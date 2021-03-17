import instructions.base
import rtda

def _aload(frame:rtda.Frame, index):
    ref = frame.LocalVars().GetRef(index)
    frame.OperandStack().PushRef(ref)

class ALOAD(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _aload(frame, self.Index)

class ALOAD_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _aload(frame, 0)

class ALOAD_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _aload(frame, 1)

class ALOAD_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _aload(frame, 2)

class ALOAD_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _aload(frame, 3)

def _dload(frame:rtda.Frame, index):
    val = frame.LocalVars().GetDouble(index)
    frame.OperandStack().PushDouble(val)

class DLOAD(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _dload(frame, self.Index)

class DLOAD_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dload(frame, 0)

class DLOAD_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dload(frame, 1)

class DLOAD_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dload(frame, 2)

class DLOAD_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dload(frame, 3)

def _fload(frame:rtda.Frame, index):
    val = frame.LocalVars().GetFloat(index)
    frame.OperandStack.PushFloat(val)

class FLOAD(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _floag(frame, self.Index)

class FLOAD_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fload(frame, 0)

class FLOAD_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fload(frame, 1)

class FLOAD_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fload(frame, 2)

class FLOAD_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _fload(frame, 3)

def _iload(frame:rtda.Frame, index):
    val = frame.LocalVars().GetInt(index)
    frame.OperandStack().PushInt(val)

class ILOAD(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _iload(frame, self.Index)

class ILOAD_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _iload(frame, 0)

class ILOAD_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _iload(frame, 1)

class ILOAD_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _iload(frame, 2)

class ILOAD_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _iload(frame, 3)

def _lload(frame:rtda.Frame, index):
    val = frame.LocalVars().GetLong(index)
    frame.OperandStack().PushLong(val)

class LLOAD(instructions.base.Index8Instruction):
    def Execute(self, frame:rtda.Frame):
        _lload(frame, self.Index)

class LLOAD_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lload(frame, 0)

class LLOAD_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lload(frame, 1)

class LLOAD_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lload(frame, 2)

class LLOAD_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _lload(frame, 3)
