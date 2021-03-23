import struct
import instructions.base
import rtda

class DADD(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = statk.PopDouble()
        result = v1 + v2
        stack.PushDouble(result)
        
class FADD(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = statk.PopFloat()
        result = v1 + v2
        stack.PushFloat(result)

class IADD(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 + v2
        stack.PushInt(result)

class LADD(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 + v2
        stack.PushLong(result)

class IAND(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = statk.PopInt()
        result = v1 and v2
        stack.PushInt(result)

class LAND(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = statk.PopLong()
        result = v1 and v2
        stack.PushLong(result)

class DDIV(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = statk.PopDouble()
        result = v1 / v2
        stack.PushDouble(result)

class FDIV(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = statk.PopFloat()
        result = v1 / v2
        stack.PushFloat(result)

class IDIV(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = statk.PopInt()
        if v2 == 0:
            raise("java.lang.ArithmeticException: / by zero")
        result = v1 / v2
        stack.PushInt(result)

class LDIV(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = statk.PopLong()
        if v2 == 0:
            raise("java.lang.ArithmeticException: / by zero")
        result = v1 / v2
        stack.PushLong(result)

class IINC:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        self.Index = reader.ReadUint8()
        self.Const = reader.ReadInt8()

    def Execute(self, frame:rtda.Frame):
        localVars = frame.LocalVars()
        val = localVars.GetInt(self.Index)
        val += self.Const
        localVars.SetInt(self.Index, val)

class DMUL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        v2 = stack.PopDouble()
        v1 = statk.PopDouble()
        result = v1 * v2
        stack.PushDouble(result)
        
class FMUL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        v2 = stack.PopFloat()
        v1 = statk.PopFloat()
        result = v1 * v2
        stack.PushFloat(result)
        
class IMUL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        v2 = stack.PopInt()
        v1 = statk.PopInt()
        result = v1 * v2
        stack.PushInt(result)
        
class LMUL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        v2 = stack.PopLong()
        v1 = statk.PopLong()
        result = v1 * v2
        stack.PushLong(result)
        
class DNEG(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        val = stack.PopDouble()
        stack.PushDouble(-val)

class FNEG(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        val = stack.PopFloat()
        stack.PushDouble(-val)

class INEG(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        val = stack.PopInt()
        stack.PushDouble(-val)

class LNEG(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        val = stack.PopLong()
        stack.PushDouble(-val)

class IOR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 or v2
        stack.PushInt(result)

class LOR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 or v2
        stack.PushLong(result)

class DREM(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = statk.PopDouble()
        result = v1 % v2
        stack.PushDouble(result)

class FREM(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = statk.PopFloat()
        result = v1 % v2
        stack.PushFloat(result)

class IREM(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        if v2 == 0:
            raise("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.PushInt(result)

class LREM(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        if v2 == 0:
            raise("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.PushLong(result)

class ISHL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        bits = struct.pack('>i', v2)
        s = struct.unpack('>I', bits)[0] & 0x3f
        result = v1 << s
        stack.PushInt(result)

class ISHR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        bits = struct.pack('>i', v2)
        s = struct.unpack('>I', bits)[0] & 0x3f
        result = v1 >> s
        stack.PushInt(result)

class IUSHR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        bits = struct.pack('>i', v2)
        s = struct.unpack('>I', bits)[0] & 0x1f
        bits1 = struct.pack('>i', v1)
        s1 = struct.unpack('>I', bits1)[0]
        result = struct.unpack('>i', struct.pack('>I',s1 >> s))[0]
        stack.PushInt(result)

class LSHL(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopLong()
        bits = struct.pack('>i', v2)
        s = struct.unpack('>I', bits)[0] & 0x3f
        result = v1 << s
        stack.PushLong(result)

class LSHR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopLong()
        bits = struct.pack('>i', v2)
        s = struct.unpack('>I', bits)[0] & 0x3f
        result = v1 >> s
        stack.PushLong(result)

class LUSHR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopLong()
        bits = struct.pack('>i', v2)
        s = struct.unpack('>I', bits)[0] & 0x1f
        bits1 = struct.pack('>l', v1)
        s1 = struct.unpack('>L', bits1)[0]
        result = struct.unpack('>l', struct.pack('>L',s1 >> s))[0]
        stack.PushInt(result)

class DSUB(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = stack.PopDouble()
        result = v1 - v2
        stack.PushDouble(result)

class FSUB(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = stack.PopFloat()
        result = v1 - v2
        stack.PushFloat(result)

class ISUB(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 - v2
        stack.PushInt(result)

class LSUB(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 - v2
        stack.PushLong(result)

class IXOR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 ^ v2
        stack.PushInt(result)

class LXOR(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 ^ v2
        stack.PushLong(result)
