import instructions.base
import rtda

class POP:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        stack.PopSlot()

class POP2:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        stack.PopSlot()
        stack.PopSlot()

class DUP:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot = stack.PopSlot()
        stack.PushSlot(slot)
        stack.PushSlot(slot)

class DUP_X1:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
        stack.PushSLot(slot1)

class DUP_X2:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSLot(slot1)

class DUP2:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
        stack.PushSLot(slot1)

class DUP2_X1:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSLot(slot1)

class DUP2_X2:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        slot4 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot4)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSLot(slot1)

class SWAP:
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
