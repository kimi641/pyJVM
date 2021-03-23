import classfile

class SymRef:
    def __init__(self):
        self._class = None

    def ResolvedClass(self):
        if self._class == None:
            self.resolveClassRef()
        return self._class

    def resolveClassRef(self):
        d = self.cp._class
        c = d.loader.LoadClass(self.className)
        if not c.isAccessibleTo(d):
            raise ValueError("java.lang.IllegalAccessError")
        self._class = c

class ClassRef(SymRef):
    pass

def newClassRef(cp,
                classInfo:classfile.ConstantClassInfo) -> ClassRef:
    ref = ClassRef()
    ref.cp = cp
    ref.className = classInfo.Name
    return ref

def lookupMethodInClass(_class, name:str, descriptor:str):
    c = _class
    while c != None:
        for method in c.methods:
            if method.name == name and \
               method.descriptor == descriptor:
                return method
        c = c.superClass
    return None

def lookupMethod(_class, name:str, descriptor:str):
    method = lookupMethodInClass(_class, name, descriptor)
    if method == None:
        method = lookupMethodInInterfaces(_class.interfaces, name, descriptor)
    return method

def lookupMethodInInterfaces(ifaces, name:str, descriptor:str):
    for iface in ifaces:
        for method in iface.methods:
            if method.name == name and \
               method.descriptor == descriptor:
                return method
        method = lookupMethodInInterfaces(iface.interfaces, name, descriptor)
        if method != None:
            return method
    return None

class MemberRef(SymRef):
    def copyMemberRefInfo(self, refInfo:classfile.ConstantMemberrefInfo):
        self.className = refInfo.ClassName
        self.name, self.descriptor = refInfo.NameAndDescriptor

    def resolveMethodRef(self):
        d = self.cp._class
        c = self.ResolvedClass()
        if c.IsInterface():
            raise ValueError("java.lang.IncompativleClassChangeError")

        method = lookupMethod(c, self.name, self.descriptor)
        if method == None:
            raise ValueError("java.lang.NoSuchMethodError")
        if not method.isAccessibleTo(d):
            raise ValueError("java.lang.IllegalAccessError")

        self.method = method

    def ResolvedMethod(self):
        if self.method == None:
            self.resolveMethodRef()
        return self.method

    def Name(self) -> str:
        return self.name

    def Descriptor(self) -> str:
        return self.descriptor

def lookupField(c, name:str, descriptor:str):
    for field in c.fields:
        if field.name == name and field.descriptor == descriptor:
            return field

    for iface in c.interfaces:
        field = lookupField(iface, name, descriptor)
        if field != None:
            return field

    if c.superClass != None:
        return lookupField(c.superClass, name, descriptor)

    return None

class FieldRef(MemberRef):
    def __init__(self):
        super().__init__()
        self.field = None

    def resolveFieldRef(self):
        d = self.cp._class
        c = self.ResolvedClass()
        field = lookupField(c, self.name, self.descriptor)

        if field == None:
            raise ValueError("java.lang.NoSuchFieldError")

        if not field.isAccessibleTo(d):
            raise ValueError("java.lang.IllegalAccessError")

        self.field = field

    def ResolvedField(self):
        if self.field == None:
            self.resolveFieldRef()
        return self.field

def newFieldRef(cp,
                refInfo:classfile.ConstantFieldrefInfo) -> FieldRef:
    ref = FieldRef()
    ref.cp = cp
    ref.copyMemberRefInfo(refInfo)
    return ref

class MethodRef(MemberRef):
    def __init__(self):
        super().__init__()
        self.method = None

    def ResolvedMethod(self):
        if self.method == None:
            self.resolveMethodRef()
        return self.method

    def resolveMethodRef(self):
        d = self.cp._class
        c = self.ResolvedClass()
        if c.IsInterface():
            raise ValueError("java.lang.IncompatibleClassChangeError")

        method = lookupMethod(c, self.name, self.descriptor)
        if method == None:
            raise ValueError("java.lang.NoSuchMethodError")
        if not method.isAccessibleTo(d):
            raise ValueError("java.lang.IllegalAccessError")

        self.method = method

def newMethodRef(cp,
                 refInfo:classfile.ConstantMethodrefInfo) -> MethodRef:
    ref = MethodRef()
    ref.cp = cp
    ref.copyMemberRefInfo(refInfo)
    return ref

def lookupInterfaceMethod(iface, name:str, descriptor:str):
    for method in iface.methods:
        if method.name == name and \
           method.descriptor == descriptor:
            return method
        return lookupMethodInInterfaces(iface.interfaces, name, descriptor)

class InterfaceMethodRef(MemberRef):
    def __init__(self):
        super().__init__()
        self.method = None

    def resolveInterfaceMethodRef(self):
        d = self.cp._class
        c = self.ResolvedClass()
        if not c.IsInterface():
            raise ValueError("java.lang.IncompatibleClassChangeError")
        method = lookupInterfaceMethod(c, self.name, self.descriptor)
        if method == None:
            raise ValueError("java.lang.NoSuchMethodError")
        if not method.isAccessibleTo(d):
            raise ValueError("java.lang.IllegalAccessError")

        self.method = method

    def ResolvedInterfaceMethod(self):
        if self.method == None:
            self.resolveInterfaceMethodRef()
        return self.method

def newInterfaceMethodRef(cp,
                          refInfo:classfile.ConstantInterfaceMethodrefInfo) -> InterfaceMethodRef:
    ref = InterfaceMethodRef()
    ref.cp = cp
    ref.copyMemberRefInfo(refInfo)
    return ref
