import struct

class ClassReader:
    def __init__(self,data:bytes):
        self.data = data

    def readUint8(self):
        #print (self.data[0])
        #val = struct.unpack('>B',self.data[0])[0]
        val = self.data[0]
        self.data = self.data[1:]
        return val

    def readUint16(self,signed=False):
        val = self.data[:2]
        self.data = self.data[2:]
        if signed:
            val = struct.unpack('>h',val)[0]
        else:
            val = struct.unpack('>H',val)[0]
        return val

    def readUint32(self):
        val = self.data[:4]
        self.data = self.data[4:]
        return val

    def readUint64(self):
        val = self.data[:8]
        self.data = self.data[8:]
        return val

    def readUint16s(self):
        n = self.readUint16()
        s = []
        for i in range(n):
            s.append(self.readUint16())
        return s

    def readBytes(self,n):
        bs = self.data[:n]
        self.data = self.data[n:]
        return bs
