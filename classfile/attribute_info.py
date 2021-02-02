import struct
from typing import List
from abc import ABCMeta, abstractmethod

from .class_read import ClassReader
from .constant_pool import ConstantPool

class AttributeInfo(metaclass=ABCMeta):
    @abstractmethod
    def readInfo(self,reader:ClassReader):
        pass

class UnparsedAttribute(AttributeInfo):
    def __init__(self, name, length, info):
        self.name = name
        self.length = length
        self.info = info

    def readInfo(self, reader:ClassReader):
        self.info = reader.readBytes(self.length)

class MarkerAttribute(AttributeInfo):
    def __init__(self):
        self.attribute_name_index = None
        self.attribute_length = None

    def readInfo(self, reader:ClassReader):
        pass

class DeprecatedAttribute(MarkerAttribute):
    pass

class SyntheticAttribute(MarkerAttribute):
    pass

class SourceFileAttribute(AttributeInfo):
    def __init__(self, cp:ConstantPool):
        self.cp = cp

    def readInfo(self, reader:ClassReader):
        self.sourceFileIndex = reader.readUint16()

    @property
    def FileName(self) -> str:
        return self.cp.getUtf8(self.sourceFileIndex)

class ConstantValueAttribute(AttributeInfo):
    def readInfo(self, reader:ClassReader):
        self.constantValueIndex = reader.readUint16()

    @property
    def ConstantValueIndex(self) -> int:
        return self.constantValueIndex

class ExceptionTableEntry:
    def __init__(self, startPc, endPc, handlerPc, catchType):
        self.startPc = startPc
        self.endPc = endPc
        self.handlerPc = handlerPc
        self.catchType = catchType

def readExceptionTable(reader:ClassReader) -> List[ExceptionTableEntry]:
    exceptionTableLength = reader.readUint16()
    exceptionTable = []
    for i in range(exceptionTableLength):
        exceptionTable.append(ExceptionTableEntry(
            startPc     = reader.readUint16(),
            endPc       = reader.readUint16(),
            handlerPc   = reader.readUint16(),
            catchType   = reader.readUint16()))
    return exceptionTable

class ExceptionsAttribute(AttributeInfo):
    def readInfo(self, reader:ClassReader):
        self.exceptionIndexTable = reader.readUint16s()

    @property
    def ExceptionIndexTable(self):
        return self.exceptionIndexTable

class CodeAttribute(AttributeInfo):
    def __init__(self, cp:ConstantPool):
        self.cp = cp

    def readInfo(self, reader:ClassReader):
        self.maxStack = reader.readUint16()
        self.maxLocals = reader.readUint16()
        codeLength = struct.unpack('>I',reader.readUint32())[0]
        self.code = reader.readBytes(codeLength)
        self.exceptionTable = readExceptionTable(reader)
        self.attributes = readAttributes(reader, self.cp)

class LineNumberTableEntry:
    def __init__(self, startPc, lineNumber):
        self.startPc = startPc
        self.lineNumber = lineNumber

class LineNumberTableAttribute(AttributeInfo):
    def readInfo(self, reader:ClassReader):
        lineNumberTableLength = reader.readUint16()
        self.lineNumberTable = []
        for i in range(lineNumberTableLength):
            self.lineNumberTable.append(LineNumberTableEntry(
                startPc     = reader.readUint16(),
                lineNumber  = reader.readUint16()))

def newAttributeInfo(attrName:str, attrLen:int, cp:ConstantPool) -> AttributeInfo:
    if attrName == "Code":
        return CodeAttribute(cp)
    elif attrName == "ConstantValue":
        return ConstantValueAttribute()
    elif attrName == "Deprecated":
        return DeprecatedAttribute()
    elif attrName == "Exceptions":
        return ExceptionsAttribute()
    elif attrName == "LineNumberTable":
        return LineNumberTableAttribute()
    elif attrName == "LocalVariableTable":
        return LocalVariableTableAttribute()
    elif attrName == "SourceFile":
        return SourceFileAttribute(cp)
    elif attrName == "Synthetic":
        return SyntheticAttribute()
    else:
        return UnparsedAttribute(attrName, attrLen, None)

def readAttribute(reader:ClassReader, cp:ConstantPool) -> AttributeInfo:
    attrNameIndex = reader.readUint16()
    attrName = cp.getUtf8(attrNameIndex)
    attrLen = struct.unpack('>I',reader.readUint32())[0]
    attrInfo = newAttributeInfo(attrName, attrLen, cp)
    attrInfo.readInfo(reader)
    return attrInfo

def readAttributes(reader:ClassReader, cp:ConstantPool) -> List[AttributeInfo]:
    attributesCount = reader.readUint16()
    attributes = []
    for i in range(attributesCount):
        attributes.append(readAttribute(reader, cp))
    return attributes

