import rtda.heap

class MethodDescriptor:
    def __init__(self):
        self.parameterTypes = []

    def addParameterType(self, t:str):
        self.parameterTypes.append(t)

class MethodDescriptorParser:
    def __init__(self):
        self.offset = 0

    def causePanic(self):
        raise ValueError(f"BAD descriptor: {self.raw}")

    def readUint8(self):
        b = self.raw[self.offset]
        self.offset += 1
        return b

    def unreadUint8(self):
        self.offset -= 1

    def startParams(self):
        if self.readUint8() != '(':
            self.causePanic()

    def endParams(self):
        if self.readUint8() != ')':
            self.causePanic()

    def finish(self):
        if self.offset != len(self.raw):
            self.causePanic()

    def parseObjectType(self) -> str:
        unread = self.raw[self.offset:]
        semicolonIndex = unread.index(';')
        if semicolonIndex == -1:
            self.causePanic()
            return ""
        else:
            objStart = self.offset - 1
            objEnd = self.offset + semicolonIndex + 1
            self.offset = objEnd
            descriptor = self.raw[objStart:objEnd]
            return descriptor

    def parseArrayType(self) -> str:
        arrStart = self.offset - 1
        self.parseFieldType()
        arrEnd = self.offset
        descriptor = self.raw[arrStart:arrEnd]
        return descriptor

    def parseFieldType(self) -> str:
        b = self.readUint8()
        if b == 'B':
            return "B"
        elif b == 'C':
            return "C"
        elif b == 'D':
            return "D"
        elif b == 'F':
            return "F"
        elif b == 'I':
            return "I"
        elif b == 'J':
            return "J"
        elif b == 'S':
            return "S"
        elif b == 'Z':
            return "Z"
        elif b == 'L':
            return self.parseObjectType()
        elif b == '[':
            return self.parseArrayType()
        else:
            self.unreadUint8()
            return ""

    def parseParamTypes(self):
        while True:
            t = self.parseFieldType()
            if t != "":
                self.parsed.addParameterType(t)
            else:
                break

    def parseReturnType(self):
        if self.readUint8() == 'V':
            self.parsed.returnType = "V"
            return
        self.unreadUint8()
        t = self.parseFieldType()
        if t != "":
            self.parsed.returnType =t
            return
        self.causePanic()

    def parse(self, descriptor:str):
        self.raw = descriptor
        self.parsed = MethodDescriptor()
        self.startParams()
        self.parseParamTypes()
        self.endParams()
        self.parseReturnType()
        self.finish()
        return self.parsed


def parseMethodDescriptor(descriptor:str) -> MethodDescriptor:
    parser = MethodDescriptorParser()
    return parser.parse(descriptor)

