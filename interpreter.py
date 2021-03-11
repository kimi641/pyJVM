import classfile
import instructions
import instructions.base
import rtda

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

def interpret(methodInfo: classfile.MemberInfo):
    codeAttr = methodInfo.CodeAttribute
    maxLocals = codeAttr.maxLocals
    maxStack = codeAttr.maxStack
    bytecode = codeAttr.code

    thread = rtda.NewThread()
    frame = thread.NewFrame(maxLocals, maxStack)
    thread.PushFrame(frame)

    try:
        loop(thread, bytecode)
    except:
        print(f"LocalVars: {frame.LocalVars()[1].num}")
        print(f"OperandStack: {frame.OperandStack()}")
