import sys
import argparse
import classpath
import classfile

from rtda import heap
from interpreter import interpret

__version__ = "0.0.1"
__author__ = "shiyi.liu"

def loadClass(className:str, cp:classpath.Classpath) -> classfile.ClassFile:
    classData, _, err = cp.ReadClass(className)
    if err != None:
        raise IOError(err)
    cf, err = classfile.Parse(classData)
    if err != None:
        raise ValueError(err)
    return cf

def printClassInfo(cf: classfile.ClassFile):
    print (f"version: {cf.MajorVersion}.{cf.MinorVersion}")
    print (f"constants count: {len(cf.ConstantPool)}")
    print (f"access flag: {cf.AccessFlags}")
    print (f"this class: {cf.ClassName}")
    print (f"super class: {cf.SuperClassName}")
    print (f"interfaces: {cf.InterfaceNames}")
    print (f"fiels count: {len(cf.Fields)}")
    for f in cf.Fields:
        print (f" {f.Name()}")
    print (f"methods count: {len(cf.Methods)}")
    for m in cf.Methods:
        print (f" {m.Name()}")

def getMainMethod(cf:classfile.ClassFile) -> classfile.MemberInfo:
    for m in cf.Methods:
        if m.Name == "main" and m.Descriptor == "([Ljava/lang/String;)V":
            return m
    return None

def startJVM(args):
    cp = classpath.Parse(args.Xjre, args.classpath)
    print(f"classpath:{cp}, class{args.Class}, args: {args}")
    classLoader = heap.NewClassLoader(cp)
    className = args.Class.replace(".","/")
    #cf = loadClass(className, cp)
    mainClass = classLoader.LoadClass(className)
    mainMethod = mainClass.GetMainMethod()
    if mainMethod != None:
        interpret(mainMethod)
    else:
        print(f"Main method not found in class {args.Class}")
    #printClassInfo(cf)
    #classData, _, err = cp.ReadClass(className)
    #classData = [int.from_bytes(x,byteorder='big',signed=False) for x in classData]
    #for x in classData:
    #    print(x, end=' ')
    #if err != None:
    #    print(f"Could not find or load main class {args.Class}")
    #    return
    #print(f"classdata:{classData}")

def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-?","--help", help="print help message")
    parser.add_argument("-v","--version", action="version", version="%(prog)s 0.0.1", help="print version and exit")
    parser.add_argument("-cp","--classpath", help="classpath")
    parser.add_argument("--Xjre", help="memory")
    parser.add_argument("Class", type=str, help="class")
    args = parser.parse_args()
    startJVM(args)

if __name__ == "__main__":
    main()
