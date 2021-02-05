import struct

from classfile.class_read import ClassReader
from classfile.cp_variables import *

CONSTANT_Class              = 7
CONSTANT_Fieldref           = 9
CONSTANT_Methodref          = 10
CONSTANT_InterfaceMethodref = 11
CONSTANT_String             = 8
CONSTANT_Integer            = 3
CONSTANT_Float              = 4
CONSTANT_Long               = 5
CONSTANT_Double             = 6
CONSTANT_NameAndType        = 12
CONSTANT_Utf8               = 1
CONSTANT_MethodHandle       = 15
CONSTANT_MethodType         = 16
CONSTANT_InvokeDynamic      = 18

def newConstantInfo(tag, cp) -> ConstantInfo:
    if tag == CONSTANT_Integer:
        return ConstantIntegerInfo()
    elif tag == CONSTANT_Float:
        return ConstantFloatInfo()
    elif tag == CONSTANT_Long:
        return ConstantLongInfo()
    elif tag == CONSTANT_Double:
        return ConstantDoubleInfo()
    elif tag == CONSTANT_Utf8:
        return ConstantUtf8Info()
    elif tag == CONSTANT_String:
        return ConstantStringInfo(cp)
    elif tag == CONSTANT_Class:
        return ConstantClassInfo(cp)
    elif tag == CONSTANT_Fieldref:
        return ConstantFieldrefInfo(ConstantMemberrefInfo(cp))
    elif tag == CONSTANT_Methodref:
        return ConstantMethodrefInfo(ConstantMemberrefInfo(cp))
    elif tag == CONSTANT_InterfaceMethodref:
        return ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo(cp))
    elif tag == CONSTANT_NameAndType:
        return ConstantNameAndTypeInfo()
    elif tag == CONSTANT_MethodType:
        return ConstantMethodTypeInfo()
    elif tag == CONSTANT_MethodHandle:
        return ConstantMethodHandleInfo()
    elif tag == CONSTANT_InvokeDynamic:
        return ConstantInvokeDynamicInfo()
    else:
        raise ValueError("java.lang.ClassFormatError: constant pool tag!")

def readConstantInfo(reader:ClassReader, cp) -> ConstantInfo:
    tag = reader.readUint8()
    c = newConstantInfo(tag, cp)
    c.readInfo(reader)
    return c
