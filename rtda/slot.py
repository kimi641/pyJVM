import struct
class Slot:
    def __init__(self):
        self.num = 0
        self.ref = None

class LocalVars(list):
    def SetInt(self, index:int, val: int):
        self[index].num = val

    def GetInt(self, index:int) -> int:
        return self[index].num

    def SetFloat(self, index:int, val:float):
        bits = struct.pack('>f',val)
        self[index].num = struct.unpack('>i',bits)[0]

    def GetFloat(self, index:int) -> float:
        bits = struct.pack('>i',self[index].num)
        return struct.unpack('>f',bits)[0]

    def SetLong(self, index:int, val:int):
        self[index].num = val & 4294967295
        self[index+1].num = val >> 32

    def GetLong(self, index:int) -> int:
        low = self[index].num
        high = self[index+1].num
        return high << 32 | low

    def SetDouble(self, index:int, val:float):
        bits = struct.pack('>d',val)
        self.SetLong(index, struct.unpack('>q',bits)[0])

    def GetDouble(self, index:int) -> float:
        bits = struct.pack('>q',self.GetLong(index))
        return struct.unpack('>d',bits)[0]

    def SetRef(self, index:int, ref):
        self[index].ref = ref

    def GetRef(self, index:int):
        return self[index].ref

    def SetSlot(self, index:int, slot:Slot):
        self[index] = slot

def newLocalVars(maxLocals:int):
    if maxLocals > 0:
        lv = LocalVars()
        for i in range(maxLocals):
            lv.append(Slot())
        return lv
    return None

class OperandStack:
    def __init__(self, slots):
        self.size = 0
        self.slots = slots

    def PushInt(self, val:int):
        self.slots[self.size].num = val
        self.size += 1

    def PopInt(self) -> int:
        self.size -= 1
        return self.slots[self.size].num

    def PushFloat(self, val:float):
        bits = struct.pack('>f', val)
        self.slots[self.size].num = struct.unpack('>i', bits)[0]
        self.size += 1

    def PopFloat(self) -> float:
        self.size -= 1
        bits = struct.pack('>i', self.slots[self.size].num)
        return struct.unpack('>f', bits)[0]

    def PushLong(self, val:int):
        self.slots[self.size].num = val & 4294967295
        self.slots[self.size+1].num = val >> 32
        self.size += 2
        
    def PopLong(self) -> int:
        self.size -= 2
        low = self.slots[self.size].num
        high = self.slots[self.size+1].num
        return high << 32 | low

    def PushDouble(self, val:float):
        bits = struct.pack('>d', val)
        self.PushLong(struct.unpack('>q',bits)[0])

    def PopDouble(self) -> float:
        bits = struct.pack('>q', self.PopLong())
        return struct.unpack('>d', bits)[0]

    def PushRef(self, ref):
        self.slots[self.size].ref = ref
        self.size += 1

    def PopRef(self):
        self.size -= 1
        ref = self.slots[self.size].ref
        self.slots[self.size].ref = None
        return ref

    def PushSlot(self, slot:Slot):
        self.slots[self.size] = slot
        self.size += 1

    def PopSlot(self):
        self.size -= 1
        return self.slots[self.size]

    def GetRefFromTop(self, n:int):
        return self.slots[self.size-1-n].ref

def newOperandStack(maxStack:int) -> OperandStack:
    if maxStack > 0:
        slots = []
        for i in range(maxStack):
            slots.append(Slot())
        return OperandStack(slots)
    return None
