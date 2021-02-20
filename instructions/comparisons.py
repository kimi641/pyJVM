import instructions.base
import rtda

def _dcmp(frame:rtda.Frame,gFlag:bool):
    statck = frame.OperandStack()
    v2 = stack.PopDouble()
    v1 = stack.PopDouble()
    if v1 > v2:
        stack.PushInt(1)
    elif v1 == v2:
        stack.PushInt(0)
    elif v1 < v2:
        stack.PushInt(-1)
    else:
        stack.PushInt(-1)

class DCMPG(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dcmp(frame, True)

class DCMPL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dcmp(frame, False)

def _fcmp(frame:rtda.Frame,gFlag:bool):
    statck = frame.OperandStack()
    v2 = stack.PopFloat()
    v1 = stack.PopFloat()
    if v1 > v2:
        stack.PushInt(1)
    elif v1 == v2:
        stack.PushInt(0)
    elif v1 < v2:
        stack.PushInt(-1)
    else:
        stack.PushInt(-1)

class FCMPG(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dcmp(frame, True)

class FCMPL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        _dcmp(frame, False)

def _acmp(frame:rtda.Frame) -> bool:
    stack = frame.OperandStack()
    ref2 = stack.PopRef()
    ref1 = stack.PopRef()
    return ref1 == ref2 #todo

class IF_ACMPEQ(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        if _acmp(frame):
            instructions.base.Branch(frame, self.Offset)

class IF_ACMPNE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        if !_acmp(frame):
            instructions.base.Branch(frame, self.Offset)

def _icmpPop(frame:rtda.Frame):
    stack = frame.OperandStack()
    val2 = stack.PopInt()
    val1 = stack.PopInt()
    return val1,val2

class IF_ICMPEQ(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val1,val2 = _icmpPop(frame)
        if val1 == val2:
            instructions.base.Branch(frame, self.Offset)

class IF_ICMPNE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val1,val2 = _icmpPop(frame)
        if val1 != val2:
            instructions.base.Branch(frame, self.Offset)

class IF_ICMPLT(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val1,val2 = _icmpPop(frame)
        if val1 < val2:
            instructions.base.Branch(frame, self.Offset)

class IF_ICMPLE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val1,val2 = _icmpPop(frame)
        if val1 <= val2:
            instructions.base.Branch(frame, self.Offset)

class IF_ICMPGT(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val1,val2 = _icmpPop(frame)
        if val1 > val2:
            instructions.base.Branch(frame, self.Offset)

class IF_ICMPGE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val1,val2 = _icmpPop(frame)
        if val1 >= val2:
            instructions.base.Branch(frame, self.Offset)

class IFEQ(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val = frame.OperandStack().PopInt()
        if val == 0:
            instructions.base.Branch(frame, self.Offset)

class IFNE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val = frame.OperandStack().PopInt()
        if val != 0:
            instructions.base.Branch(frame, self.Offset)

class IFLT(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val = frame.OperandStack().PopInt()
        if val < 0:
            instructions.base.Branch(frame, self.Offset)

class IFLE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val = frame.OperandStack().PopInt()
        if val <= 0:
            instructions.base.Branch(frame, self.Offset)

class IFGT(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val = frame.OperandStack().PopInt()
        if val > 0:
            instructions.base.Branch(frame, self.Offset)

class IFGE(instructions.base.BranchInstuction):
    def Execute(self, frame:rtda.Frame):
        val = frame.OperandStack().PopInt()
        if val >= 0:
            instructions.base.Branch(frame, self.Offset)

class LCMP(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        if v1 > v2:
            stack.PushInt(1)
        elif v1 == v2:
            stack.PushInt(0)
        else:
            stack.PushInt(-1)
