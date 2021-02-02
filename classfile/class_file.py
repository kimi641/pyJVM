import sys
import struct

from typing import List

from .class_read import ClassReader
from .member_info import readMembers
from .constant_pool import readConstantPool
from .attribute_info import readAttributes

class ClassFile:
    def __init__(self):
        self.minorVersion = None
        self.majroVersion = None
        self.constantPool = None
        self.accessFlags = None
        self.thisClass = None
        self.superClass = None
        self.interfaces = None
        self.fields = None
        self.methods = None
        self.attributes = None

    def readAndCheckMagic(self,reader):
        magic = reader.readUint32()
        if magic != b'\xca\xfe\xba\xbe':
            raise TypeError("java.lang.ClassFormatError: magic!")

    def readAndCheckVersion(self,reader):
        self.minorVersion = reader.readUint16()
        self.majorVersion = reader.readUint16()
        if self.majorVersion == 45:
            return
        elif self.majorVersion in (46,47,48,49,50,51,52):
            if self.minorVersion == 0:
                return
        raise TypeError("java.lang.UnsupprotedClassVersionError!")

    @property
    def MinorVersion(self):
        return self.minorVersion

    @property
    def MajorVersion(self):
        return self.majorVersion

    @property
    def ConstantPool(self):
        return self.constantPool

    @property
    def AccessFlags(self):
        return self.accessFlags

    @property
    def Fields(self):
        return self.fields

    @property
    def Methods(self):
        return self.methods

    @property
    def ClassName(self) -> str:
        return self.constantPool.getClassName(self.thisClass)

    @property
    def SuperClassName(self) -> str:
        if self.superClass > 0:
            return self.constantPool.getClassName(self.superClass)
        return ""

    @property
    def InterfaceNames(self) -> List[str]:
        interfaceNames = []
        for cpIndex in self.interfaces:
            interfaceNames.append(self.constantPool.getClassName(cpIndex))
        return interfaceNames

    def read(self, reader:ClassReader):
        self.readAndCheckMagic(reader)
        self.readAndCheckVersion(reader)
        self.constantPool = readConstantPool(reader)
        self.accessFlags = reader.readUint16()
        self.thisClass = reader.readUint16()
        self.superClass = reader.readUint16()
        self.interfaces = reader.readUint16s()
        self.fields = readMembers(reader, self.constantPool)
        self.methods = readMembers(reader, self.constantPool)
        self.attributes = readAttributes(reader, self.constantPool)

def Parse(classData:bytes):
    try:
        cr = ClassReader(classData)
        cf = ClassFile()
        cf.read(cr)
    except ValueError as err:
        print(sys.exc_info())
        return None,err
    return cf,None
