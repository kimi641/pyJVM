import struct
from abc import ABCMeta, abstractmethod

class BytecodeReader:
    def Reset(self, code, pc:int):
        self.code = code
        self.pc = pc

    def ReadUint8(self):
        i = self.code[self.pc]
        self.pc += 1
        return i

    def ReadInt8(self):
        byte = struct.pack('>B',self.ReadUint8())
        return struct.unpack('>b',byte)[0]

    def ReadUint16(self):
        bits = self.code[self.pc:self.pc+2]
        self.pc += 2
        return struct.unpack('>H',bits)[0]

    def ReadInt16(self):
        bits = self.code[self.pc:self.pc+2]
        self.pc += 2
        return struct.unpack('>h',bits)[0]

    def ReadInt32(self):
        bits = self.code[self.pc:self.pc+4]
        self.pc += 4
        return struct.unpack('>i',bits)[0]
        
    def ReadInt32s(self):
        pass

    def SkipPadding(self):
        pass

    @property
    def PC(self):
        return self.pc

class Instruction(metaclass=ABCMeta):

    @abstractmethod
    def FetchOperands(self, reader:BytecodeReader):
        pass

    @abstractmethod
    def Execute(self, frame):
        pass

class NoOperandsInstruction(Instruction):
    def FetchOperands(self, reader:BytecodeReader):
        pass

class BranchInstruction(Instruction):
    def FetchOperands(self, reader:BytecodeReader):
        self.Offset = reader.ReadInt16()

class Index8Instruction(Instruction):
    def FetchOperands(self, reader:BytecodeReader):
        self.Offset = reader.ReadUint8()

class Index16Instruction(Instruction):
    def FetchOperands(self, reader:BytecodeReader):
        self.Offset = reader.ReadUint16()
