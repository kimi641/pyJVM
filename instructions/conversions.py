import struct

import instructions.base
import rtda

class D2F(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        d = stack.PopDoulbe()
        f = struct.unpack('>f',struct.pack('>d',d))[0]
        stack.pushFloat(f)

class D2I(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        d = stack.PopDoulbe()
        i = struct.unpack('>i',struct.pack('>d',d))[0]
        stack.pushInf(i)

class D2L(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        d = stack.PopDoulbe()
        l = struct.unpack('>q',struct.pack('>d',d))[0]
        stack.pushInf(l)

class F2D(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        f = stack.PopFloat()
        d = struct.unpack('>d', struct.pack('>f',f))[0]
        stack.pushDoulbe(d)

class F2I(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        f = stack.PopFloat()
        i = struct.unpack('>i', struct.pack('>f',f))[0]
        stack.pushDoulbe(i)

class F2L(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        f = stack.PopFloat()
        l = struct.unpack('>q', struct.pack('>f',f))[0]
        stack.pushDoulbe(l)

class I2B(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        b = struct.unpack('>b', struct.pack('>i',i))[0]
        stack.pushInt(b)

class I2C(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        c = struct.unpack('>c', struct.pack('>i',i))[0]
        stack.pushInt(c)

class I2S(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        s = struct.unpack('>h', struct.pack('>i',i))[0]
        stack.pushInt(s)

class I2L(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        l = struct.unpack('>q', struct.pack('>i',i))[0]
        stack.pushInt(l)

class I2F(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        f = struct.unpack('>f', struct.pack('>i',i))[0]
        stack.pushInt(f)

class I2D(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        d = struct.unpack('>d', struct.pack('>i',i))[0]
        stack.pushInt(d)

class L2D(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        l = stack.PopLong()
        d = struct.unpack('>d', struct.pack('>q',l))[0]
        stack.pushInt(d)

class L2F(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        l = stack.PopLong()
        f = struct.unpack('>f', struct.pack('>q',l))[0]
        stack.pushInt(f)

class L2I(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        l = stack.PopLong()
        i = struct.unpack('>i', struct.pack('>q',l))[0]
        stack.pushInt(i)
