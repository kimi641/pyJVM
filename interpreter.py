import classfile
import instructions
import instructions.base
import rtda
import rtda.heap

def logInstruction(frame:rtda.Frame, inst:instructions.base.Instruction):
    method = frame.Method()
    className = method.Class().Name()
    methodName = method.Name()
    pc = frame.Thread().PC()
    print(f"{className}.{methodName} #{pc} {inst} {inst}")

def loop(thread:rtda.Thread, logInst:bool):
    reader = instructions.base.BytecodeReader()
    while True:
        frame = thread.CurrentFrame()
        pc = frame.NextPC
        thread.SetPC(pc)
        #decode
        reader.Reset(frame.Method().Code(), pc)
        opcode = reader.ReadUint8()
        inst = instructions.NewInstruction(opcode)
        inst.FetchOperands(reader)
        frame.SetNextPC(reader.PC)

        if logInst:
            logInstruction(frame, inst)

        #execute
        #print(f"pc:{pc} inst:{inst}")
        inst.Execute(frame)
        if thread.IsStackEmpty():
            break

def logFrames(thread:rtda.Thread):
    while not thread.IsStackEmpty():
        frame = thread.PopFrame()
        method = frame.Method()
        className = method.Class().Name()
        print(f">> pc:{frame.NextPC} {className}.{method.Name()}{method.Descriptor()}")

def interpret(method: rtda.heap.Method, logInst:bool):
    thread = rtda.NewThread()
    frame = thread.NewFrame(method)
    thread.PushFrame(frame)

    #try:
    loop(thread, logInst)
    #except:
    #    logFrames(thread)
