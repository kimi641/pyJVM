import instructions.base
import rtda
import rtda.heap

#Create new object

class NEW(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        _class = classRef.ResolvedClass()

        if _class.IsInterface() or _class.IsAbstract():
            raise ValueError("java.lang.InstantiationError")

        ref = _class.NewObject()
        frame.OperandStack().PushRef(ref)

class PUT_STATIC(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        currentMethod = frame.Method()
        currentClass = currentMethod.Class()
        cp = currentClass.ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()
        _class = field.Class()

        if not field.IsStatic():
            raise ValueError("java.lang.IncompatibleClassChangeError")
        if field.IsFinal():
            if currentClass != _class or currentMethod.Nmae() != "<clinit>":
                raise ValueError("java.lang.IllegalAccessError")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        slots = _class.StaticVars()
        stack = frame.OperandStack()

        if descriptor[0] in ['Z','B','C','S','I']:
            slots.SetInt(slotId, stack.PopInt())
        elif descriptor[0] == 'F':
            slots.SetFloat(slotId, stack.PopFloat())
        elif descriptor[0] == 'J':
            slots.SetLong(slotId, stack.PopLong())
        elif descriptor[0] == 'D':
            slots.SetDouble(slotId, stack.PopDouble())
        elif descriptor[0] in ['L', '[']:
            slots.SetRef(slotId, stack.PopRef())

class GET_STATIC(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        cp = frame.Method().Class().ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()
        _class = field.Class()

        if not field.IsStatic():
            raise ValueError("java.lang.IncompatibleClassChangeError")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        slots = _class.StaticVars()
        stack = frame.OperandStack()

        if descriptor[0] in ['Z','B','C','S','I']:
            stack.PushInt(slots.GetInt(slotId))
        elif descriptor[0] == 'F':
            stack.PushFloat(slots.GetFloat(slotId))
        elif descriptor[0] == 'J':
            stack.PushLong(slots.GetLong(slotId))
        elif descriptor[0] == 'D':
            stack.PushDouble(slots.GetDouble(slotId))
        elif descriptor[0] in ['L', '[']:
            stack.PushRef(slots.GetRef(slotId))

class PUT_FIELD(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        currentMethod = frame.Method()
        currentClass = currentMethod.Class()
        cp = currentClass.ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()

        if field.IsStatic():
            raise ValueError("java.lang.IncompatibleClassChangeError")

        if field.IsFinal():
            if currentClass != field.Class() or currentMethod.Nmae() != "<init>":
                raise ValueError("java.lang.IllegalAccessError")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        stack = frame.OperandStack()

        if descriptor[0] in ['Z','B','C','S','I']:
            val = stack.PopInt()
            ref = stack.PopRef()
            if ref == None:
                raise ValueError("java.lang.NullPointerException")
            ref.Fields().SetInt(slotId, val)
        elif descriptor[0] == 'F':
            val = stack.PopFloat()
            ref = stack.PopFloat()
            if ref == None:
                raise ValueError("java.lang.NullPointerException")
            ref.Fields().SetFloat(slotId, val)
        elif descriptor[0] == 'J':
            val = stack.PopLong()
            ref = stack.PopLong()
            if ref == None:
                raise ValueError("java.lang.NullPointerException")
            ref.Fields().SetLong(slotId, val)
        elif descriptor[0] == 'D':
            val = stack.PopDouble()
            ref = stack.PopDouble()
            if ref == None:
                raise ValueError("java.lang.NullPointerException")
            ref.Fields().SetDouble(slotId, val)
        elif descriptor[0] in ['L', '[']:
            val = stack.PopRef()
            ref = stack.PopRef()
            if ref == None:
                raise ValueError("java.lang.NullPointerException")
            ref.Fields().SetRef(slotId, val)

class GET_FIELD(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        cp = frame.Method().Class().ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()

        if field.IsStatic():
            raise ValueError("java.lang.IncompatibleClassChangeError")
        
        stack = frame.OperandStack()
        ref = stack.PopRef()
        if ref == None:
            raise ValueError("java.lang.NullPointerException")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        slots = ref.Fields()

        if descriptor[0] in ['Z','B','C','S','I']:
            stack.PushInt(slots.GetInt(slotId))
        elif descriptor[0] == 'F':
            stack.PushFloat(slots.GetFloat(slotId))
        elif descriptor[0] == 'J':
            stack.PushLong(slots.GetLong(slotId))
        elif descriptor[0] == 'D':
            stack.PushDouble(slots.GetDouble(slotId))
        elif descriptor[0] in ['L', '[']:
            stack.PushRef(slots.GetRef(slotId))

class INSTANCE_OF(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        ref = stack.PopRef()
        if ref == None:
            stack.PushInt(0)
            return

        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        _class = classRef.ResolvedClass()

        if ref.IsInstanceOf(_class):
            stack.PushInt(1)
        else:
            stack.PushInt(0)

# Check whether object is of given type
class CHECK_CAST(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        stack = frame.OperandStack()
        ref = stack.PopRef()
        stack.PushRef(ref)
        if ref == None:
            return

        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        _class = classRef.ResolvedClass()
        if not ref.IsInstanceOf(_class):
            raise ValueError("java.lang.ClassCastException")

# hack
class INVOKE_SPECIAL(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        ref = frame.OperandStack().PopRef()

# hack
class INVOKE_VIRTUAL(instructions.base.Index16Instruction):
    def Execute(self, frame:rtda.Frame):
        cp = frame.Method().Class().ConstantPool()
        methodRef = cp.GetConstant(self.Index)
        if methodRef.Name() == "println":
            stack = frame.OperandStack()
            if methodRef.Descriptor() == "(Z)V":
                print(f"{stack.PopInt() != 0}")
            elif methodRef.Descriptor() == "(C)V":
                print(f"{stack.PopInt()}")
            elif methodRef.Descriptor() == "(B)V":
                print(f"{stack.PopInt()}")
            elif methodRef.Descriptor() == "(S)V":
                print(f"{stack.PopInt()}")
            elif methodRef.Descriptor() == "(I)V":
                print(f"{stack.PopInt()}")
            elif methodRef.Descriptor() == "(J)V":
                print(f"{stack.PopLong()}")
            elif methodRef.Descriptor() == "(F)V":
                print(f"{stack.PopFloat()}")
            elif methodRef.Descriptor() == "(D)V":
                print(f"{stack.PopDouble()}")
            else:
                raise ValueError(f"println: {methodRef.Descriptor()}")
            stack.PopRef()
