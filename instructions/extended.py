import instructions.base
import instructions.loads
import instructions.math
import instructions.stores
import rtda

class GOTO_W:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        self.offset = int(reader.ReadInt32())

    def Execute(self, frame:rtda.Frame):
        base.Branch(frame, self.offset)

class IFNULL(instructions.base.BranchInstruction):
    def Execute(self, frame:rtda.Frame):
        ref = frame.OperandStack().PopRef()
        if ref == None:
            base.Branch(frame, self.Offset)

class IFNONNULL(instructions.base.BranchInstruction):
    def Execute(self, frame:rtda.Frame):
        ref = frame.OperandStack().PopRef()
        if ref != None:
            base.Branch(frame, self.Offset)

class WIDE:
    def FetchOperands(self, reader:instructions.base.BytecodeReader):
        opcode = reader.ReadUint8()
        if opcode == 0x15:
            inst = instructions.loads.ILOAD()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x16:
            inst = instructions.loads.LLOAD()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x17:
            inst = instructions.loads.FLOAD()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x18:
            inst = instructions.loads.DLOAD()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x19:
            inst = instructions.loads.ALOAD()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x36:
            inst = instructions.stores.ISTORE()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x37:
            inst = instructions.stores.LSTORE()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x38:
            inst = instructions.stores.FSTORE()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x39:
            inst = instructions.stores.DSTORE()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x3a:
            inst = instructions.stores.ASTORE()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0x84:
            inst = instructions.math.IINC()
            ints.Index = reader.readUint16()
            self.modifiedInstruction = inst
        elif opcode == 0xa9:
            raise("Unsupported opcode: 0xa9!")

    def Execute(self, frame:rtda.Frame):
        self.modifiedInstruction.Execute(frame)
