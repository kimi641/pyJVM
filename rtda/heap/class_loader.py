from typing import List,Tuple

import classfile
import classpath

from rtda.heap.object import Class, newClass, Field
from rtda.slot import LocalVars as Slots, newLocalVars as newSlots

def parseClass(data:List) -> Class:
    cf, err = classfile.Parse(data)
    if err != None:
        raise ValueError("java.lang.ClassFormatError")
    return newClass(cf)

def resolveSuperClass(_class:Class):
    if _class.name != "java/lang/Object":
        _class.superClass = _class.loader.LoadClass(_class.superClassName)

def resolveInterfaces(_class:Class):
    interfaceCount = len(_class.interfaceNames)
    if interfaceCount > 0:
        _class.interfaces = []
        for interfaceName in _class.interfaceNames:
            _class.interfaces.append(_class.loader.LoadClass(interfaceName))

def verify(_class:Class):
    pass

def calcInstanceFieldSlotIds(_class:Class):
    slotId = 0
    if _class.superClass != None:
        slotId = _class.superClass.instanceSlotCount
    for field in _class.fields:
        if not field.IsStatic():
            field.soltId = slotId
            slotId += 1
            if field.isLongOrDouble():
                slotId += 1
    _class.instanceSlotCount = slotId

def calcStaticFieldSlotIds(_class:Class):
    slotId = 0
    for field in _class.fields:
        if field.IsStatic():
            field.slotId = slotId
            slotId += 1
            if field.isLongOrDouble():
                slotId += 1
    _class.saticSlotCount = slotId

def initStaticFinalVar(_class:Class, field:Field):
    _vars = _class.staticVars
    cp = _class.constantPool
    cpIndex = field.ConstValueIndex()
    slotId = field.SlotId()

    if cpIndex > 0:
        if field.Descriptor() in ["Z","B","C","S","I"]:
            val = cp.GetConstant(cpIndex)
            _vars.SetInt(slotId, val)
        elif field.Descriptor() == "J":
            val = cp.GetConstant(cpIndex)
            _vars.SetLong(slotId, val)
        elif field.Descriptor() == "F":
            val = cp.GetConstant(cpIndex)
            _vars.SetFloat(slotId, val)
        elif field.Descriptor() == "D":
            val = cp.GetConstant(cpIndex)
            _vars.SetDouble(slotId, val)
        elif field.Descriptor() == "Ljava/lang/String":
            raise ValueError("todo")

def allocAndInitStaticVars(_class:Class):
    _class.staticVars = newSlots(_class.saticSlotCount)
    for field in _class.fields:
        if field.IsStatic() and field.IsFinal():
            initStaticFinalVar(_class, field)

def perpare(_class:Class):
    calcInstanceFieldSlotIds(_class)
    calcStaticFieldSlotIds(_class)
    allocAndInitStaticVars(_class)

def link(_class:Class):
    verify(_class)
    perpare(_class)

class ClassLoader:
    def __init__(self,cp:classpath.Classpath,verboseFlag:bool,classMap:List[Class]):
        self.cp = cp
        self.verboseFlag = verboseFlag
        self.classMap = classMap

    def LoadClass(self, name:str) -> Class:
        if name in self.classMap:
            return self.classMap[name]
        return self.loadNonArrayClass(name)

    def loadNonArrayClass(self, name:str) -> Class:
        data, entry = self.readClass(name)
        _class = self.defineClass(data)
        link(_class)
        if self.verboseFlag:
            print(f"[Loaded {name} from {entry}]")
        return _class

    def readClass(self, name:str) -> Tuple[List, classpath.Entry]:
        data, entry, err = self.cp.ReadClass(name)
        if err != None:
            raise ValueError(f"java.lang.ClassNotFoundExeception: {name}")
        return data, entry

    def defineClass(self, data:List) -> Class:
        _class = parseClass(data)
        _class.loader = self
        resolveSuperClass(_class)
        resolveInterfaces(_class)
        self.classMap[_class.name] = _class
        return _class

def NewClassLoader(cp:classpath.Classpath, verboseFlag:bool) -> ClassLoader:
    return ClassLoader(cp,verboseFlag,{})
