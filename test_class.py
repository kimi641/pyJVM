class ConstantPool(list):
    def foo(self):
        print("foo")

a = ConstantPool()
a.foo()

class A:
    def __init__(self):
        self.var = 1

b = [A()] * 5
b[0].var = 5
print(b[4].var)
