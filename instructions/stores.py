import instructions.base
import rtda

def _lstore(frame: jvm.rtda.Frame, index):
    val = frame.OperandStack().PopLong()
    frame.LocalVars().SetLong(index, val)

class LSTORE:
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, self.Index)

class LSTORE_0:
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 0)

class LSTORE_1:
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 1)

class LSTORE_2:
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 2)

class LSTORE_3:
    def Execute(self, frame:rtda.Frame):
        _lstore(frame, 3)
