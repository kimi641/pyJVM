import instructions.base
import rtda

class NOP(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        pass

class ACONST_NULL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushRef(None)

class DCONST_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushDouble(0.0)

class DCONST_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushDouble(1.0)

class FCONST_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushFloat(0.0)

class FCONST_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushFloat(1.0)

class FCONST_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushFloat(2.0)

class ICONST_M1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(-1)

class ICONST_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(0)

class ICONST_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(1)

class ICONST_2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(2)

class ICONST_3(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(3)

class ICONST_4(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(4)

class ICONST_5(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushInt(5)

class LCONST_0(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushLong(0)

class LCONST_1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        frame.OperandStack().PushLong(1)

class BIPUSH:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        self.val = reader.ReadInt8()

    def Execute(self, frame:rtda.Frame):
        i = int(self.val)
        frame.OperandStack().PushInt(i)

class SIPUSH:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        sefl.val = reader.ReadInt16()

    def Execute(self, frame:rtda.Frame):
        i = int(self.val)
        frame.OperandStack().PushInt(i)
