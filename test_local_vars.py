from jvm import rtda

def testLocalVars(var):
    var.SetInt(0, 100)
    var.SetInt(1, -100)
    var.SetLong(2, 2997924580)
    var.SetLong(4, -2997924580)
    var.SetFloat(6, 3.1415925)
    var.SetDouble(7, 2.71828182845)
    var.SetRef(9, None)
    print(var.GetInt(0))
    print(var.GetInt(1))
    print(var.GetLong(2))
    print(var.GetLong(4))
    print(var.GetFloat(6))
    print(var.GetDouble(7))
    print(var.GetRef(9))

frame = rtda.newFrame(100,100)
testLocalVars(frame.LocalVars)
