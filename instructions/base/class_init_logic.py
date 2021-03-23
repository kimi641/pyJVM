import instructions.base
import rtda
import rtda.heap

def scheduleClinit(thread:rtda.Thread, _class:rtda.heap.Class):
    clinit = _class.GetClinitMethod()
    if clinit != None:
        # exec<clinit>
        newFrame = thread.NewFrame(clinit)
        thread.PushFrame(newFrame)

def initSuperClass(thread:rtda.Thread, _class:rtda.heap.Class):
    if not _class.IsInterface():
        superClass = _class.SuperClass()
        if superClass != None and not superClass.InitStarted():
            InitClass(thread, superClass)

def InitClass(thread:rtda.Thread, _class:rtda.heap.Class):
    _class.StartInit()
    scheduleClinit(thread, _class)
    initSuperClass(thread, _class)
