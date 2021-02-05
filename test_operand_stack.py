from jvm import rtda

def testOperandStack(ops):
    ops.PushInt(100)
    ops.PushInt(-100)
    ops.PushLong(2997924580)
    ops.PushLong(-2997924580)
    ops.PushFloat(3.1415925)
    ops.PushDouble(2.71828182845)
    ops.PushRef(None)
    print(ops.PopRef())
    print(ops.PopDouble())
    print(ops.PopFloat())
    print(ops.PopLong())
    print(ops.PopLong())
    print(ops.PopInt())
    print(ops.PopInt())

frame = rtda.newFrame(100,100)
testOperandStack(frame.OperandStack)
