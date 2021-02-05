import struct
from abc import ABCMeta, abstractmethod

from typing import Tuple
from classfile.class_read import ClassReader

class ConstantInfo(metaclass=ABCMeta):
    @abstractmethod
    def readInfo(self,reader:ClassReader):
        pass

class ConstantIntegerInfo(ConstantInfo):
    def readInfo(self,reader:ClassReader):
        bts = reader.readUint32()
        self.val = struct.unpack('>i',bts)[0]

class ConstantFloatInfo(ConstantInfo):
    def readInfo(self,reader:ClassReader):
        bts = reader.readUint32()
        self.val = struct.unpack('>f',bts)[0]

class ConstantLongInfo(ConstantInfo):
    def readInfo(self,reader:ClassReader):
        bts = reader.readUint64()
        self.val = struct.unpack('>q',bts)[0]

class ConstantDoubleInfo(ConstantInfo):
    def readInfo(self,reader:ClassReader):
        bts = reader.readUint64()
        self.val = struct.unpack('>d',bts)[0]

class ConstantUtf8Info(ConstantInfo):
    def readInfo(self,reader:ClassReader):
        length = reader.readUint16()
        bts = reader.readBytes(length)
        self.str = bts.decode('utf-8')

class ConstantStringInfo(ConstantInfo):
    def __init__(self,cp):
        self.cp = cp

    def readInfo(self,reader:ClassReader):
        self.stringIndex = reader.readUint16()

    @property
    def String(self) -> str:
        return self.cp.getUtf8(self.stringIndex)

class ConstantClassInfo(ConstantInfo):
    def __init__(self,cp):
        self.cp = cp

    def readInfo(self,reader:ClassReader):
        self.nameIndex = reader.readUint16()

    @property
    def Name(self) -> str:
        return self.cp.getUtf8(self.nameIndex)

class ConstantNameAndTypeInfo(ConstantInfo):
    def readInfo(self,reader:ClassReader):
        self.nameIndex = reader.readUint16()
        self.descriptorIndex = reader.readUint16()

class ConstantMemberrefInfo(ConstantInfo):
    def __init__(self,cp):
        self.cp = cp

    def readInfo(self,reader:ClassReader):
        self.classIndex = reader.readUint16()
        self.nameAndTypeIndex = reader.readUint16()

    @property
    def ClassName(self) -> str:
        return self.cp.getClassName(self.classIndex)

    @property
    def NameAndDescriptor(self) -> Tuple[str,str]:
        return self.cp.getNameAndType(self.nameAndTypeIndex)

class ConstantFieldrefInfo(ConstantMemberrefInfo):pass

class ConstantMethodrefInfo(ConstantMemberrefInfo):pass

class ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo):pass
