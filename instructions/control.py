import instructions.base
import rtda

class GOTO(instructions.base.BranchInstruction):
    def Execute(self, frame:rtda.Frame):
        instructions.base.Branch(frame, self.Offset)

class LOOKUP_SWITCH:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        reader.SkipPadding()
        self.defaultOffset = reader.ReadInt32()
        self.npairs = reader.ReadInt32()
        self.matchOffsets = reader.ReadInt32s(self.npairs * 2)

    def Execute(self, frame:rtda.Frame):
        key = frame.OperandStack().PopInt()
        for i in range(0,self.npairs * 2,2):
            if self.matchOffsets[i] == key:
                offset = self.matchOffsets[i+1]
                instructions.base.Branch(frame, int(offset))
                return
        instructions.base.Branch(frame, int(self.defaultOffset))

class TABLE_SWITCH:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        reader.SkipPadding()
        self.defaultOffset = reader.ReadInt32()
        self.low = reader.ReadInt32()
        self.high = reader.ReadInt32()
        jumpOffsetCount = self.high - self.low + 1
        self.jumpOffsets = reader.ReadInt32s(jumpOffsetsCount)

    def Execute(self, frame:rtda.Frame):
        index = frame.OperandStack().PopInt()

        offset = 0
        if index >= self.low and index <= self.high:
            offset = int(self.jumpOffsets[index-self.low])
        else:
            offset = int(self.defaultOffset)
        instructions.base.Branch(frame, offset)

class RETURN(instructions.base.NoOperandsInstruction): # Return void
    def Execute(self, frame:rtda.Frame):
        frame.Thread().PopFrame()

class ARETURN(instructions.base.NoOperandsInstruction): # Return reference
    def Execute(self, frame:rtda.Frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        ref = currentFrame.OperandStack().PopRef()
        invokerFrame.OperandStack().PushRef(ref)

class DRETURN(instructions.base.NoOperandsInstruction): # Return double
    def Execute(self, frame:rtda.Frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        retVal = currentFrame.OperandStack().PopDouble()
        invokerFrame.OperandStack().PushDouble(retVal)

class FRETURN(instructions.base.NoOperandsInstruction): # Return float
    def Execute(self, frame:rtda.Frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        retVal = currentFrame.OperandStack().PopFloat()
        invokerFrame.OperandStack().PushFloat(retVal)

class IRETURN(instructions.base.NoOperandsInstruction): # Return Int
    def Execute(self, frame:rtda.Frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        retVal = currentFrame.OperandStack().PopInt()
        invokerFrame.OperandStack().PushInt(retVal)

class LRETURN(instructions.base.NoOperandsInstruction): # Return Long
    def Execute(self, frame:rtda.Frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        retVal = currentFrame.OperandStack().PopLong()
        invokerFrame.OperandStack().PushLong(retVal)

