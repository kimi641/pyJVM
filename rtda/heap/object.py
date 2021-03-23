from typing import List

import classfile
from rtda.slot import LocalVars as Slots, newLocalVars as newSlots
from rtda.heap.cp import newClassRef, newFieldRef, newMethodRef, newInterfaceMethodRef
from rtda.heap.method_descriptor import *

ACC_PUBLIC          = 0x0001 #class field method
ACC_PRIVATE         = 0x0002 #      field method
ACC_PROTECTED       = 0x0004 #      field method
ACC_STATIC          = 0x0008 #      field method
ACC_FINAL           = 0x0010 #class field method
ACC_SUPER           = 0x0020 #class
ACC_SYNCHRONIZED    = 0x0020 #            method
ACC_VOLATILE        = 0x0040 #      field
ACC_BRIDGE          = 0x0040 #            method
ACC_TRANSIENT       = 0x0080 #      field
ACC_VARARGS         = 0x0080 #            method
ACC_NATIVE          = 0x0100 #            method
ACC_INTERFACE       = 0x0200 #class
ACC_ABSTRACT        = 0x0400 #class       method
ACC_STRICT          = 0x0800 #            method
ACC_SYNTHETIC       = 0x1000 #class field method
ACC_ANNOTATION      = 0x2000 #class
ACC_ENUM            = 0x4000 #class field

class Object:
    def __init__(self, _class, fields):
        self._class = _class
        self.fields = fields

    def Class(self):
        return self._class

    def Fields(self):
        return self.fields

    def IsInstanceOf(self,_class) -> bool:
        return _class.isAssignableFrom(self._class)

def newObject(_class):
    return Object(_class = _class,
                  fields = newSlots(_class.instanceSlotCount))

class Class:
    def __init__(self):
        self.superClass = None
        self.interfaces = []
        self.initStarted = False

    def IsPublic(self) -> bool:
        return 0 != self.accessFlags & ACC_PUBLIC

    def IsFinal(self) -> bool:
        return 0 != self.accessFlags & ACC_FINAL

    def IsSuper(self) -> bool:
        return 0 != self.accessFlags & ACC_SUPER

    def IsInterface(self) -> bool:
        return 0 != self.accessFlags & ACC_INTERFACE

    def IsAbstract(self) -> bool:
        return 0 != self.accessFlags & ACC_ABSTRACT

    def IsSynthetic(self) -> bool:
        return 0 != self.accessFlags & ACC_SYNTHETIC

    def IsAnnotation(self) -> bool:
        return 0 != self.accessFlags & ACC_ANNOTATION

    def IsEnum(self) -> bool:
        return 0 != self.accessFlags & ACC_ENUM

    def isAssignableFrom(self, other) -> bool:
        s, t = other, self
        if s == t:
            return True
        if not t.IsInterface():
            return s.isSubClassOf(t)
        else:
            return s.isImplements(t)

    def IsSubClassOf(self, other) -> bool:
        c = self.superClass
        while c != None:
            c = c.superClass
            if c == other:
                return True
        return False

    def IsImplements(self, iface) -> bool:
        c = self
        while c != None:
            for i in c.interfaces:
                if i == iface or i.isSubInterfaceOf(iface):
                    return True
            c = c.superClass
        return False

    def isSubInterfaceOf(self, iface) -> bool:
        for superInterface in self.interfaces:
            if superInterface == iface or superInterface.isSubInterfaceOf(iface):
                return True
        return False

    def IsSuperClassOf(self, other) -> bool:
        return other.IsSubClassOf(self)

    def Name(self):
        return self.name

    def Field(self):
        return self.fields

    def Methods(self):
        return self.methods

    def ConstantPool(self):
        return self.constantPool

    def SuperClass(self):
        return self.superClass

    def StaticVars(self):
        return self.staticVars

    def InitStarted(self) -> bool:
        return self.initStarted

    def StartInit(self):
        self.initStarted = True

    def isAccessibleTo(self, other) -> bool:
        return self.IsPublic() or self.getPackageName() == other.getPackageName()

    def getpackageName(self) -> str:
        i = self.name.rindex("/")
        if i >= 0:
            return self.name[:i]
        return ""

    def getStaticMethod(self, name, descriptor:str):
        for method in self.methods:
            if method.IsStatic() and \
                method.name == name and \
                method.descriptor == descriptor:
                return method
        return None

    def GetMainMethod(self):
        return self.getStaticMethod("main", "([Ljava/lang/String;)V")

    def GetClinitMethod(self):
        return self.getStaticMethod("<clinit>", "()V")

    def NewObject(self):
        return newObject(self)

def newClass(cf: classfile.ClassFile) -> Class:
    _class = Class()
    _class.accessFlags = cf.AccessFlags
    _class.name = cf.ClassName
    _class.superClassName = cf.SuperClassName
    _class.interfaceNames = cf.InterfaceNames
    _class.constantPool = newConstantPool(_class, cf.ConstantPool)
    _class.fields = newFields(_class, cf.Fields)
    _class.methods = newMethods(_class, cf.Methods)
    return _class

class ClassMember:
    def copyMemberInfo(self, memberInfo: classfile.MemberInfo):
        self.accessFlags = memberInfo.AccessFlags
        self.name = memberInfo.Name
        self.descriptor = memberInfo.Descriptor

    def IsPublic(self) -> bool:
        return 0 != self.accessFlags & ACC_PUBLIC

    def IsPrivate(self) -> bool:
        return 0 != self.accessFlags & ACC_PRIVATE

    def IsProtected(self) -> bool:
        return 0 != self.accessFlags & ACC_PROTECTED

    def IsStatic(self) -> bool:
        return 0 != self.accessFlags & ACC_STATIC

    def IsFinal(self) -> bool:
        return 0 != self.accessFlags & ACC_FINAL

    def IsSynthetic(self) -> bool:
        return 0 != self.accessFlags & ACC_SYNTHETIC

    def Name(self) -> str:
        return self.name

    def Descriptor(self) -> str:
        return self.descriptor

    def Class(self) -> str:
        return self._class

    def isAccessibleTo(self, d:Class) -> bool:
        if self.IsPublic():
            return True

        c = self._class
        if self.IsProtected():
            return d == c or d.isSubClassOf(c) or \
                   c.getPackageName() == d.getPackageName()
        if not self.IsPrivate():
            return c.getPackageName() == d.getPackageName()
        return d == c

class Field(ClassMember):
    def __init__(self):
        self.constValueIndex = 0
        self.slotId = 0

    def copyAttributes(self, cfField:classfile.MemberInfo):
        valAttr = cfField.ConstantValueAttribute()
        if valAttr != None:
            self.constValueIndex = valAttr.ConstantValueIndex()

    def IsVolatile(self) -> bool:
        return 0 != self.accessFlags & ACC_VOLATILE

    def IsTransient(self) -> bool:
        return 0 != self.accessFlags & ACC_TRASIENT

    def IsEnum(self) -> bool:
        return 0 != self.accessFlags & ACC_ENUM

    def ConstValueIndex(self):
        return self.constValueIndex

    def SlotId(self):
        return self.slotId

    def isLongOrDouble(self) -> bool:
        return self.descriptor == "J" or self.descriptor == "D"

def newFields(_class:Class, cfFields:List[classfile.MemberInfo]) -> List[Field]:
    fields = []
    for cfField in cfFields:
        field = Field()
        field._class = _class
        field.copyMemberInfo(cfField)
        field.copyAttributes(cfField)
        fields.append(field)
    return fields

class Method(ClassMember):
    def __init__(self):
        super().__init__()
        self.maxStack = 0
        self.maxLocals = 0
        self.argSlotCount = 0

    def copyAttributes(self, cfMethod:classfile.MemberInfo):
        codeAttr = cfMethod.CodeAttribute
        if codeAttr != None:
            self.maxStack = codeAttr.MaxStack
            self.maxLocals = codeAttr.MaxLocals
            self.code = codeAttr.Code

    def IsSynchronized(self) -> bool:
        return 0 != self.accessFlags & ACC_SYNCHRONIZED

    def IsBridge(self) -> bool:
        return 0 != self.accessFlags & ACC_BRIDGE

    def IsVarargs(self) -> bool:
        return 0 != self.accessFlags & ACC_VARARGS

    def IsNative(self) -> bool:
        return 0 != self.accessFlags & ACC_NATIVE

    def IsAbstract(self) -> bool:
        return 0 != self.accessFlags & ACC_ABSTRACT

    def IsStrict(self) -> bool:
        return 0 != self.accessFlags & ACC_STRICT

    def MaxStack(self):
        return self.maxStack

    def MaxLocals(self):
        return self.maxLocals

    def Code(self):
        return self.code

    def ArgSlotCount(self):
        return self.argSlotCount

    def calcArgSlotCount(self):
        parsedDescriptor = parseMethodDescriptor(self.descriptor)
        for paramType in parsedDescriptor.parameterTypes:
            self.argSlotCount += 1
            if paramType == "J" or paramType == "D":
                self.argSlotCount += 1
        if not self.IsStatic():
            self.argSlotCount += 1

def newMethods(_class:Class, cfMethods: List[classfile.MemberInfo]) -> List[Method]:
    methods = []
    for cfMethod in cfMethods:
        method = Method()
        method._class = _class
        method.copyMemberInfo(cfMethod)
        method.copyAttributes(cfMethod)
        method.calcArgSlotCount()
        methods.append(method)
    return methods

class ConstantPool:
    def __init__(self, _class, consts):
        self._class = _class
        self.consts = consts

    def GetConstant(self, index):
        c = self.consts[index]
        if c != None:
            return c
        raise ValueError(f"No constants at index {index}")

def newConstantPool(_class:Class, cfCp:classfile.ConstantPool) -> ConstantPool:
    cpCount = len(cfCp)
    consts = [None] * cpCount
    rtCp = ConstantPool(_class,consts)
    i = 1
    while i < cpCount:
        cpInfo = cfCp[i]
        if isinstance(cpInfo, classfile.ConstantIntegerInfo):
            intInfo = cpInfo
            consts[i] = intInfo.Value()
        elif isinstance(cpInfo, classfile.ConstantFloatInfo):
            floatInfo = cpInfo
            consts[i] = floatInfo.Value()
        elif isinstance(cpInfo, classfile.ConstantLongInfo):
            longInfo = cpInfo
            consts[i] = longInfo.Value()
            i += 1
        elif isinstance(cpInfo, classfile.ConstantDoubleInfo):
            doubleInfo = cpInfo
            consts[i] = doubleInfo.Value()
            i += 1
        elif isinstance(cpInfo, classfile.ConstantStringInfo):
            stringInfo = cpInfo
            consts[i] = stringInfo.String
        elif isinstance(cpInfo, classfile.ConstantClassInfo):
            classInfo = cpInfo
            consts[i] = newClassRef(rtCp, classInfo)
        elif isinstance(cpInfo, classfile.ConstantFieldrefInfo):
            fieldrefInfo = cpInfo
            consts[i] = newFieldRef(rtCp, fieldrefInfo)
        elif isinstance(cpInfo, classfile.ConstantMethodrefInfo):
            methodrefInfo = cpInfo
            consts[i] = newMethodRef(rtCp, methodrefInfo)
        elif isinstance(cpInfo, classfile.ConstantInterfaceMethodrefInfo):
            methodrefInfo = cpInfo
            consts[i] = newInterfaceMethodRef(rtCp, methodrefInfo)
        else:
            pass
        i += 1
    return rtCp

