from rtda.slot import newLocalVars, newOperandStack
class Frame:
    def __init__(self, thread, localVars, operandStack):
        self.thread = thread
        self.LocalVars = localVars
        self.OperandStack = operandStack
        self.nextPC = 0

    @property
    def NextPC(self) -> int:
        return self.nextPC

    @nextPC.setter
    def SetNextPC(self, nextPC:int):
        self.nextPC = nextPC

def newFrame(thread, maxLocals, maxStack:int) -> Frame:
    return Frame(thread = thread,
                 localVars = newLocalVars(maxLocals),
                 operandStack = newOperandStack(maxStack))

class Stack:
    def __init__(self, maxSize:int):
        self.maxSize = maxSize
    def push(self,frame):
        if self.size >= self.maxSize:
            raise OverflowError("java.lang.StackOverflowError")
        if self._top != None:
            frame.lower = self._top
        self._top = frame
        self.size += 1

    def pop(self):
        if self._top == None:
            raise IndexError("jvm stack is empty!")
        top = self._top
        self._top = top.lower
        top.lower = None
        self.size -= 1
        return top

    def top(self):
        if self._top == None:
            raise IndexError("jvm stack is empty!")
        return self._top
    
def newStack(maxSize:int) -> Stack:
    return Stack(maxSize = maxSize)

class Thread:
    def __init__(self, stack):
        #self.pc = pc
        self.stack = stack

    @property
    def PC(self) -> int:
        return self.pc

    @PC.setter
    def SetPC(self, pc:int):
        self.pc = pc

    def PushFrame(self, frame):
        self.stack.push(frame)

    def PopFrame(self, frame):
        return self.stack.pop()

    def CurrentFrame(self, frame):
        return self.stack.top()

    def NewFrame(self, maxLocals, maxStack) -> Frame:
        return newFrame(self, maxLocals, maxStack)

def newThread() -> Thread:
    return Thread(stack = newStack(1024))