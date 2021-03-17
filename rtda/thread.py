from rtda.slot import newLocalVars, newOperandStack
import rtda.heap

class Frame:
    def __init__(self, localVars, operandStack, thread, method):
        self.lower = None
        self.localVars = localVars
        self.operandStack = operandStack
        self.thread = thread
        self.method = method
        self.nextPC = 0

    def LocalVars(self):
        return self.localVars

    def OperandStack(self):
        return self.operandStack

    def Thread(self):
        return self.thread

    def Method(self):
        return self.method

    @property
    def NextPC(self) -> int:
        return self.nextPC

    def SetNextPC(self, nextPC:int):
        self.nextPC = nextPC

def NewFrame(thread, method:rtda.heap.Method) -> Frame:
    return Frame(thread = thread,
                 method = method,
                 localVars = newLocalVars(method.MaxLocals()),
                 operandStack = newOperandStack(method.MaxStack()))

class Stack:
    def __init__(self, maxSize:int):
        self.maxSize = maxSize
        self.size = 0
        self._top = None

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
    
def NewStack(maxSize:int) -> Stack:
    return Stack(maxSize = maxSize)

class Thread:
    def __init__(self, stack):
        self.pc = 0
        self.stack = stack

    def PC(self) -> int:
        return self.pc

    def SetPC(self, pc:int):
        self.pc = pc

    def PushFrame(self, frame):
        self.stack.push(frame)

    def PopFrame(self):
        return self.stack.pop()

    def CurrentFrame(self, frame):
        return self.stack.top()

    def NewFrame(self, method:rtda.heap.Method) -> Frame:
        return NewFrame(self, method)

def NewThread() -> Thread:
    return Thread(stack = NewStack(1024))
