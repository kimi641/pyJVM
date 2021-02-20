from typing import List

from classfile.class_read import ClassReader
from classfile.attribute_info import readAttributes,CodeAttribute

class MemberInfo:
    def __init__(self,
                 cp,
                 accessFlags,
                 nameIndex,
                 descriptorIndex,
                 attributes):
        self.cp = cp
        self.accessFlags = accessFlags
        self.nameIndex = nameIndex
        self.descriptorIndex = descriptorIndex
        self.attributes = attributes

    @property
    def AccessFlags(self):
        return self.accessFlags

    def Name(self) -> str:
        return self.cp.getUtf8(self.nameIndex)
        
    def Descriptor(self) -> str:
        return self.cp.getUtf8(self.descriptorIndex)

    def CodeAttribute(self) -> CodeAttribute:
        for attrInfo in self.attributes:
            if isinstance(attrInfo,CodeAttribute):
                return attrInfo
        return None

def readMembers(reader:ClassReader, cp) -> List[MemberInfo]:
    memberCount = reader.readUint16()
    members = []
    for i in range(memberCount):
        members.append(readMember(reader, cp))
    return members
    
def readMember(reader:ClassReader, cp) -> MemberInfo:
    return MemberInfo(cp,
                      reader.readUint16(),
                      reader.readUint16(),
                      reader.readUint16(),
                      readAttributes(reader, cp))
