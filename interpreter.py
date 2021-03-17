import classfile
import instructions
import instructions.base
import rtda
import rtda.heap

def loop(thread:rtda.Thread, bytecode):
    frame = thread.PopFrame()
    reader = instructions.base.BytecodeReader()
    while True:
        pc = frame.NextPC
        thread.SetPC(pc)
        #decode
        reader.Reset(bytecode, pc)
        opcode = reader.ReadUint8()
        inst = instructions.NewInstruction(opcode)
        inst.FetchOperands(reader)
        frame.SetNextPC(reader.PC)
        #execute
        print(f"pc:{pc} inst:{inst}")
        inst.Execute(frame)

def interpret(method: rtda.heap.Method):
    thread = rtda.NewThread()
    frame = thread.NewFrame(method)
    thread.PushFrame(frame)

    #try:
    loop(thread, method.Code())
    #except:
    #    print(f"LocalVars: {frame.LocalVars()[1].num}")
    #    print(f"OperandStack: {frame.OperandStack()}")
