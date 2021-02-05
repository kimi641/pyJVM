from typing import Tuple

from classfile.class_read import ClassReader
from classfile.constant_info import readConstantInfo
from classfile.cp_variables import *

class ConstantPool(list):
    def getConstantInfo(self, index):
        cpInfo = self[index]
        if cpInfo != None:
            return cpInfo
        raise ValueError("Invalid constant pool index!")

    def getNameAndType(self,index) -> Tuple[str,str]:
        ntInfo = self.getConstantInfo(index)
        name = self.getUtf8(ntInfo.nameIndex)
        _type = self.getUtf8(ntInfo.descriptorIndex)
        return (name, _type)

    def getClassName(self,index) -> str:
        classInfo = self.getConstantInfo(index)
        return self.getUtf8(classInfo.nameIndex)

    def getUtf8(self,index) -> str:
        utf8Info = self.getConstantInfo(index)
        return utf8Info.str

def readConstantPool(reader: ClassReader) -> ConstantPool:
    cpCount = reader.readUint16()
    cp = ConstantPool([None] * cpCount)
    i = 1
    while i < cpCount:
        cp[i] = readConstantInfo(reader, cp)
        if (isinstance(cp[i], ConstantLongInfo) or
            isinstance(cp[i], ConstantDoubleInfo)):
            i += 1
        i += 1
    return cp
