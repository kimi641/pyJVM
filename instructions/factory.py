import instructions.base
from instructions.comparisons import *
from instructions.constants import *
from instructions.control import *
from instructions.conversions import *
from instructions.extended import *
from instructions.loads import *
from instructions.math import *
from instructions.stack import *
from instructions.stores import *

nop         = NOP()
aconst_null = ACONST_NULL()
iconst_m1   = ICONST_M1()
iconst_0    = ICONST_0()
iconst_1    = ICONST_1()
iconst_2    = ICONST_2()
iconst_3    = ICONST_3()
iconst_4    = ICONST_4()
iconst_5    = ICONST_5()
lconst_0    = LCONST_0()
lconst_1    = LCONST_1()
fconst_0    = FCONST_0()
fconst_1    = FCONST_1()
fconst_2    = FCONST_2()
dconst_0    = DCONST_0()
dconst_1    = DCONST_1()
iload_0     = ILOAD_0()
iload_1     = ILOAD_1()
iload_2     = ILOAD_2()
iload_3     = ILOAD_3()
lload_0     = LLOAD_0()
lload_1     = LLOAD_1()
lload_2     = LLOAD_2()
lload_3     = LLOAD_3()
fload_0     = FLOAD_0()
fload_1     = FLOAD_1()
fload_2     = FLOAD_2()
fload_3     = FLOAD_3()
dload_0     = DLOAD_0()
dload_1     = DLOAD_1()
dload_2     = DLOAD_2()
dload_3     = DLOAD_3()
aload_0     = ALOAD_0()
aload_1     = ALOAD_1()
aload_2     = ALOAD_2()
aload_3     = ALOAD_3()
istore_0    = ISTORE_0()
istore_1    = ISTORE_1()
istore_2    = ISTORE_2()
istore_3    = ISTORE_3()
lstore_0    = LSTORE_0()
lstore_1    = LSTORE_1()
lstore_2    = LSTORE_2()
lstore_3    = LSTORE_3()
fstore_0    = FSTORE_0()
fstore_1    = FSTORE_1()
fstore_2    = FSTORE_2()
fstore_3    = FSTORE_3()
dstore_0    = DSTORE_0()
dstore_1    = DSTORE_1()
dstore_2    = DSTORE_2()
dstore_3    = DSTORE_3()
astore_0    = ASTORE_0()
astore_1    = ASTORE_1()
astore_2    = ASTORE_2()
astore_3    = ASTORE_3()
pop         = POP()
pop2        = POP2()
dup         = DUP()
dup_x1      = DUP_X1()
dup_x2      = DUP_X2()
dup2        = DUP2()
dup2_x1     = DUP2_X1()
dup2_x2     = DUP2_X2()
swap        = SWAP()
iadd        = IADD()
ladd        = LADD()
fadd        = FADD()
dadd        = DADD()
isub        = ISUB()
lsub        = LSUB()
fsub        = FSUB()
dsub        = DSUB()
imul        = IMUL()
lmul        = LMUL()
fmul        = FMUL()
dmul        = DMUL()
idiv        = IDIV()
ldiv        = LDIV()
fdiv        = FDIV()
ddiv        = DDIV()
irem        = IREM()
lrem        = LREM()
frem        = FREM()
drem        = DREM()
ineg        = INEG()
lneg        = LNEG()
fneg        = FNEG()
dneg        = DNEG()
ishl        = ISHL()
ishr        = ISHR()
lshl        = LSHL()
lshr        = LSHR()
iushr       = IUSHR()
lushr       = LUSHR()
iand        = IAND()
land        = LAND()
ior         = IOR()
lor         = LOR()
ixor        = IXOR()
lxor        = LXOR()
i2l         = I2L()
i2f         = I2F()
i2d         = I2D()
l2i         = L2I()
l2f         = L2F()
l2d         = L2D()
f2i         = F2I()
f2l         = F2L()
f2d         = F2D()
d2i         = D2I()
d2l         = D2L()
d2f         = D2F()
i2b         = I2B()
i2c         = I2C()
i2s         = I2S()
lcmp        = LCMP()
fcmpl       = FCMPL()
fcmpg       = FCMPG()
dcmpl       = DCMPL()
dcmpg       = DCMPG()

def NewInstruction(opcode) -> instructions.base.Instruction:
    if opcode == 0x00:
        return nop
    elif opcode == 0x01:
        return aconst_null
    elif opcode == 0x02:
        return iconst_m1
    elif opcode == 0x03:
        return iconst_0
    elif opcode == 0x04:
        return iconst_1
    elif opcode == 0x05:
        return iconst_2
    elif opcode == 0x06:
        return iconst_3
    elif opcode == 0x07:
        return iconst_4
    elif opcode == 0x08:
        return iconst_5
    elif opcode == 0x09:
        return lconst_0
    elif opcode == 0x0a:
        return lconst_1
    elif opcode == 0x0b:
        return fconst_0
    elif opcode == 0x0c:
        return fconst_1
    elif opcode == 0x0d:
        return fconst_2
    elif opcode == 0x0e:
        return dconst_0
    elif opcode == 0x0f:
        return dconst_1
    elif opcode == 0x10:
        return BIPUSH()
    elif opcode == 0x11:
        return SIPUSH()
    #elif opcode == 0x12:
    #elif opcode == 0x13:
    #elif opcode == 0x14:
    elif opcode == 0x15:
        return ILOAD()
    elif opcode == 0x16:
        return LLOAD()
    elif opcode == 0x17:
        return FLOAD()
    elif opcode == 0x18:
        return DLOAD()
    elif opcode == 0x19:
        return ALOAD()
    elif opcode == 0x1a:
        return iload_0
    elif opcode == 0x1b:
        return iload_1
    elif opcode == 0x1c:
        return iload_2
    elif opcode == 0x1d:
        return iload_3
    elif opcode == 0x1e:
        return lload_0
    elif opcode == 0x1f:
        return lload_1
    elif opcode == 0x20:
        return lload_2
    elif opcode == 0x21:
        return lload_3
    elif opcode == 0x22:
        return fload_0
    elif opcode == 0x23:
        return fload_1
    elif opcode == 0x24:
        return fload_3
    elif opcode == 0x25:
        return dload_0
    elif opcode == 0x26:
        return dload_1
    elif opcode == 0x27:
        return dload_2
    elif opcode == 0x28:
        return dload_3
    elif opcode == 0x29:
        return aload_0
    elif opcode == 0x2a:
        return aload_1
    elif opcode == 0x2b:
        return aload_2
    elif opcode == 0x2c:
        return aload_3
    #elif opcode == 0x2d:
    #elif opcode == 0x2e:
    #elif opcode == 0x2f:
    #elif opcode == 0x31:
    #elif opcode == 0x32:
    #elif opcode == 0x33:
    #elif opcode == 0x34:
    #elif opcode == 0x35:
    elif opcode == 0x36:
        return ISTORE()
    elif opcode == 0x37:
        return LSTORE()
    elif opcode == 0x38:
        return FSTORE()
    elif opcode == 0x39:
        return DSTORE()
    elif opcode == 0x3a:
        return ASTORE()
    elif opcode == 0x3b:
        return istore_0
    elif opcode == 0x3c:
        return istore_1
    elif opcode == 0x3d:
        return istore_2
    elif opcode == 0x3e:
        return istore_3
    elif opcode == 0x3f:
        return lstore_0
    elif opcode == 0x40:
        return lstore_1
    elif opcode == 0x41:
        return lstore_2
    elif opcode == 0x42:
        return lstore_3
    elif opcode == 0x43:
        return fstore_0
    elif opcode == 0x44:
        return fstore_1
    elif opcode == 0x45:
        return fstore_2
    elif opcode == 0x46:
        return fstore_3
    elif opcode == 0x47:
        return dstore_0
    elif opcode == 0x48:
        return dstore_1
    elif opcode == 0x49:
        return dstore_2
    elif opcode == 0x4a:
        return dstore_3
    elif opcode == 0x4b:
        return astore_0
    elif opcode == 0x4c:
        return astore_1
    elif opcode == 0x4d:
        return astore_2
    elif opcode == 0x4d:
        return astore_3
    #elif opcode == 0x4f:
    #elif opcode == 0x50:
    #elif opcode == 0x51:
    #elif opcode == 0x52:
    #elif opcode == 0x53:
    #elif opcode == 0x54:
    #elif opcode == 0x55:
    #elif opcode == 0x56:
    elif opcode == 0x57:
        return pop
    elif opcode == 0x58:
        return pop2
    elif opcode == 0x59:
        return dup
    elif opcode == 0x5a:
        return dup_x1
    elif opcode == 0x5b:
        return dup_x2
    elif opcode == 0x5c:
        return dup2
    elif opcode == 0x5d:
        return dup2_x1
    elif opcode == 0x5e:
        return dup2_x2
    elif opcode == 0x5f:
        return swap
    elif opcode == 0x60:
        return iadd
    elif opcode == 0x61:
        return ladd
    elif opcode == 0x62:
        return fadd
    elif opcode == 0x63:
        return dadd
    elif opcode == 0x64:
        return isub
    elif opcode == 0x65:
        return lsub
    elif opcode == 0x66:
        return fsub
    elif opcode == 0x67:
        return dsub
    elif opcode == 0x68:
        return imul
    elif opcode == 0x69:
        return lmul
    elif opcode == 0x6a:
        return fmul
    elif opcode == 0x6b:
        return dmul
    elif opcode == 0x6c:
        return idiv
    elif opcode == 0x6d:
        return ldiv
    elif opcode == 0x6e:
        return fdiv
    elif opcode == 0x6f:
        return ddiv
    elif opcode == 0x70:
        return irem
    elif opcode == 0x71:
        return lrem
    elif opcode == 0x72:
        return frem
    elif opcode == 0x73:
        return drem
    elif opcode == 0x74:
        return ineg
    elif opcode == 0x75:
        return lneg
    elif opcode == 0x76:
        return fneg
    elif opcode == 0x77:
        return dneg
    elif opcode == 0x78:
        return ishl
    elif opcode == 0x79:
        return ishl
    elif opcode == 0x7a:
        return ishr
    elif opcode == 0x7b:
        return lshr
    elif opcode == 0x7c:
        return iushr
    elif opcode == 0x7d:
        return lushr
    elif opcode == 0x7e:
        return iand
    elif opcode == 0x7f:
        return land
    elif opcode == 0x80:
        return ior
    elif opcode == 0x81:
        return lor
    elif opcode == 0x82:
        return ixor
    elif opcode == 0x83:
        return lxor
    elif opcode == 0x84:
        return IINC()
    elif opcode == 0x85:
        return i2l
    elif opcode == 0x86:
        return i2f
    elif opcode == 0x87:
        return i2d
    elif opcode == 0x88:
        return l2i
    elif opcode == 0x89:
        return l2f
    elif opcode == 0x8a:
        return l2d
    elif opcode == 0x8b:
        return f2i
    elif opcode == 0x8c:
        return f2l
    elif opcode == 0x8d:
        return f2d
    elif opcode == 0x8e:
        return d2i
    elif opcode == 0x8f:
        return d2l
    elif opcode == 0x90:
        return d2f
    elif opcode == 0x91:
        return i2b
    elif opcode == 0x92:
        return i2c
    elif opcode == 0x93:
        return i2s
    elif opcode == 0x94:
        return lcmp
    elif opcode == 0x95:
        return fcmpl
    elif opcode == 0x96:
        return fcmpg
    elif opcode == 0x97:
        return dcmpl
    elif opcode == 0x98:
        return dcmpg
    elif opcode == 0x99:
        return IFEQ()
    elif opcode == 0x9a:
        return IFNE()
    elif opcode == 0x9b:
        return IFLT()
    elif opcode == 0x9c:
        return IFGE()
    elif opcode == 0x9d:
        return IFGT()
    elif opcode == 0x9e:
        return IFLE()
    elif opcode == 0x9f:
        return IF_ICMPEQ()
    elif opcode == 0xa0:
        return IF_ICMPNE()
    elif opcode == 0xa1:
        return IF_ICMPLT()
    elif opcode == 0xa2:
        return IF_ICMPGE()
    elif opcode == 0xa3:
        return IF_ICMPGT()
    elif opcode == 0xa4:
        return IF_ICMPLE()
    elif opcode == 0xa5:
        return IF_ACMPEQ()
    elif opcode == 0xa6:
        return IF_ACMPNE()
    elif opcode == 0xa7:
        return GOTO()
    #elif opcode == 0xa8:
    #elif opcode == 0xa9:
    elif opcode == 0xaa:
        return TABLE_SWITCH()
    elif opcode == 0xab:
        return LOOKUP_SWITCH()
    #elif opcode == 0xac:
    #elif opcode == 0xad:
    #elif opcode == 0xae:
    #elif opcode == 0xaf:
    #elif opcode == 0xb0:
    #elif opcode == 0xb1:
    #elif opcode == 0xb2:
    #elif opcode == 0xb3:
    #elif opcode == 0xb4:
    #elif opcode == 0xb5:
    #elif opcode == 0xb6:
    #elif opcode == 0xb7:
    #elif opcode == 0xb8:
    #elif opcode == 0xb9:
    #elif opcode == 0xba:
    #elif opcode == 0xbb:
    #elif opcode == 0xbc:
    #elif opcode == 0xbd:
    #elif opcode == 0xbe:
    #elif opcode == 0xbf:
    #elif opcode == 0xc0:
    #elif opcode == 0xc1:
    #elif opcode == 0xc2:
    #elif opcode == 0xc3:
    elif opcode == 0xc4:
        return WIDE()
    #elif opcode == 0xc5:
    elif opcode == 0xc6:
        return IFNULL()
    elif opcode == 0xc7:
        return IFNONNULL()
    elif opcode == 0xc8:
        return GOTO_W()
    #elif opcode == 0xc9:
    #elif opcode == 0xca:
    #elif opcode == 0xfe:
    #elif opcode == 0xff:
    else:
        raise ValueError(f"Unsupported opcode:{opcode}")
