import instructions.base
import rtda

def _astore(frame: rtda.Frame, index):
    ref = frame.OperandStack().PopRef()
    frame.LocalVars().SetRef(index, ref)

class ASTORE(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _astore(frame, self.Index)

class ASTORE_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _astore(frame, 0)

class ASTORE_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _astore(frame, 1)

class ASTORE_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _astore(frame, 2)

class ASTORE_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _astore(frame, 3)

def _dstore(frame: rtda.Frame, index):
    val = frame.OperandStack().PopDouble()
    frame.LocalVars().SetDouble(index, val)

class DSTORE(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _dstore(frame, self.Index)

class DSTORE_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dstore(frame, 0)

class DSTORE_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dstore(frame, 1)

class DSTORE_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dstore(frame, 2)

class DSTORE_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dstore(frame, 3)

def _fstore(frame: rtda.Frame, index):
    val = frame.OperandStack().PopFloat()
    frame.LocalVars().SetFloat(index, val)

class FSTORE(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _fstore(frame, self.Index)

class FSTORE_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fstore(frame, 0)

class FSTORE_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fstore(frame, 1)

class FSTORE_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fstore(frame, 2)

class FSTORE_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fstore(frame, 3)

def _istore(frame: rtda.Frame, index):
    val = frame.OperandStack().PopInt()
    frame.LocalVars().SetInt(index, val)

class ISTORE(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _istore(frame, self.Index)

class ISTORE_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _istore(frame, 0)

class ISTORE_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _istore(frame, 1)

class ISTORE_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _istore(frame, 2)

class ISTORE_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _istore(frame, 3)

def _lstore(frame: rtda.Frame, index):
    val = frame.OperandStack().PopLong()
    frame.LocalVars().SetLong(index, val)

class LSTORE(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, self.Index)

class LSTORE_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 0)

class LSTORE_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 1)

class LSTORE_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 2)

class LSTORE_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 3)
