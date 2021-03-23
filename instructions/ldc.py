import instructions.base
import rtda

def _ldc(frame: rtda.Frame, index:int):
    stack = frame.OperandStack()
    cp = frame.Method().Class().ConstantPool()
    c = cp.GetConstant(index)

    if isinstance(c,int):
        stack.PushInt(c)
    elif isinstance(c,float):
        stack.PushFloat(c)
    else:
        raise ValueError("todo: ldc!")

class LDC(instructions.base.Index8Instruction):
    def Execute(self, frame: rtda.Frame):
        _ldc(frame, self.Index)

class LDC_W(instructions.base.Index16Instruction):
    def Execute(self, frame: rtda.Frame):
        _ldc(frame, self.Index)

class LDC2_W(instructions.base.Index16Instruction):
    def Execute(self, frame: rtda.Frame):
        stack = frame.OperandStack()
        cp = frame.Method().Class().ConstantPool()
        c = cp.GetConstant(self.Index)

        if isinstance(c,int):
            stack.PushLong(c)
        elif isinstance(c,float):
            stack.PushDouble(c)
        else:
            raise ValueError("java.lang.ClassFormatError")
