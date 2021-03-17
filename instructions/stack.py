import copy

import instructions.base
import rtda

class POP(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        stack.PopSlot()

class POP2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        stack.PopSlot()
        stack.PopSlot()

class DUP(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot = stack.PopSlot()
        stack.PushSlot(slot)
        stack.PushSlot(copy.deepcopy(slot))

class DUP_X1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
        stack.PushSLot(copy.deepcopy(slot1))

class DUP_X2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSLot(copy.deepcopy(slot1))

class DUP2(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(copy.deepcopy(slot2))
        stack.PushSLot(copy.deepcopy(slot1))

class DUP2_X1(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot3)
        stack.PushSlot(copy.deepcopy(slot2))
        stack.PushSLot(copy.deepcopy(slot1))

class DUP2_X2(instructions.base.NoOperandsInstruction):
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
        stack.PushSlot(copy.deepcopy(slot2))
        stack.PushSLot(copy.deepcopy(slot1))

class SWAP(instructions.base.NoOperandsInstruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
