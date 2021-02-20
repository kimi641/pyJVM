import rtda

def Branch(frame:jvm.rtda.Frame, offset:int):
    pc = frame.Thread().PC()
    nextPC = pc + offset
    frame.SetNextPC(nextPC)
