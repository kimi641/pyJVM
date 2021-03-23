import rtda

def InvokeMethod(invokerFrame:rtda.Frame, method:rtda.heap.Method):
    thread = invokerFrame.Thread()
    newFrame = thread.NewFrame(method)
    thread.PushFrame(newFrame)

    argSlotCount = int(method.ArgSlotCount())
    if argSlotCount > 0:
        for i in range(argSlotCount-1,-1,-1):
            slot = invokerFrame.OperandStack().PopSlot()
            newFrame.LocalVars().SetSlot(i,slot)

    # hack
    if method.IsNative():
        if method.Name() == "registerNatives":
            thread.PopFrame()
        else:
            raise ValueError("native method {method.Class().Name()}.{method.Name()}{method.Descriptor()}")
