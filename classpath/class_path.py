import abc
import os
from zipfile import ZipFile
from typing import Tuple,List

PathListSeparator = ':'

class Entry(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def readClass(path:str) -> Tuple:
        pass

    @abc.abstractmethod
    def String() -> str:
        pass

class DirEntry(Entry):
    def __init__(self,path:str):
        self.absDir = path

    def readClass(self, className:str) -> Tuple[bytes,Entry,str]:
        fileName = os.path.join(self.absDir, className)
        err = None
        data = open(fileName,'rb').read()
        return (data,self,err)

    @property
    def String(self) -> str:
        return self.absDir
        
def newDirEntry(path:str) -> Entry:
    absDir = os.path.abspath(path)
    if not os.path.exists(absDir):
        raise OSError(f"No Dir:{absDir}")
    return DirEntry(absDir)

class ZipEntry(Entry):
    def __init__(self,path:str):
        self.absPath = path

    def readClass(self, className:str) -> Tuple[bytes,Entry,str]:
        with ZipFile(self.absPath) as myzip:
            if className not in myzip.namelist():
                return (None,None,f"class not found:  {className}")
        with ZipFile(self.absPath) as myzip:
            data = myzip.read(className)
            return (data,self,None)

    @property
    def String(self) -> str:
        return self.absPath

def newZipEntry(path:str):
    absPath = os.path.abspath(path)
    if not os.path.exists(absPath):
        raise OSError(f"No File:{absPath}")
    return ZipEntry(absPath)

class ComponsiteEntry(list):
    def readClass(self, className:str) -> Tuple[bytes,Entry,str]:
        for e in self:
            data, From, err = e.readClass(className)
            if err == None:
                return (data, From, None)
        return (None,None,f"class not found:  {className}")

    @property
    def String(self) -> str:
        strs = []
        for e in self:
            strs.append(e.String())
        return PathListSeparator.join(strs)

def newCompositeEntry(pathList: str):
    componsiteEntry = ComponsiteEntry()
    for path in pathList.split(PathListSeparator):
        entry = newEntry(path)
        compositeEntry = componsiteEntry.append(entry)
    return componsiteEntry

def newWildcardEntry(path: str):
    componsiteEntry = ComponsiteEntry()
    for fn in os.listdir(path[:-1]):
        filepath = os.path.join(path[:-1],fn)
        if os.path.isdir(filepath):
            continue
        elif filepath.endswith(".jar") or filepath.endswith(".JAR"):
            jarEntry = newZipEntry(filepath)
            componsiteEntry.append(jarEntry)
    return componsiteEntry

def newEntry(path:str) -> Entry:
    if ':' in path:
        return newCompositeEntry(path)
    elif path.endswith('*'):
        return newWildcardEntry(path)
    elif path.endswith(".jar") or \
         path.endswith(".JAR") or \
         path.endswith(".zip") or \
         path.endswith(".ZIP"):
        return newZipEntry(path)
    return newDirEntry(path)

class Classpath:
    def __init__(self):
        self.bootClasspath = None
        self.extClasspath = None
        self.userClasspath = None

    def ReadClass(self, className:str) -> Tuple[bytes,Entry,str]:
        className = className + ".class"
        data, entry, err = self.bootClasspath.readClass(className)
        if err == None:
            return data, entry, err
        data, entry, err = self.extClasspath.readClass(className)
        if err == None:
            return data, entry, err
        return self.userClasspath.readClass(className)

    @property
    def String(self) -> str:
        return self.userClasspath.String()

    def getJreDir(self,jreOption:str) -> str:
        if jreOption != "" and os.path.exists(jreOption):
            return jreOption
        if os.path.exists("./jre"):
            return "./jre"
        jh = os.environ["JAVA_HOME"]
        if jh != "":
            return os.path.join(jh, "jre")
        raise OSError("Can not find jre folder!")

    def parseBootAndExtClasspath(self,jreOption: str):
        jreDir = self.getJreDir(jreOption)

        # jre/lib/*
        jreLibPath = os.path.join(jreDir, "lib", "*")
        self.bootClasspath = newWildcardEntry(jreLibPath)

        # jre/lib/ext/*
        jreExtPath = os.path.join(jreDir, "lib", "ext", "*")
        self.extClasspath = newWildcardEntry(jreExtPath)

    def parseUserClasspath(self, cpOption:str):
        if cpOption == "" or cpOption == None:
            cpOption = "."
        self.userClasspath = newEntry(cpOption)

def Parse(jreOption:str, cpOption: str) -> Classpath:
    cp = Classpath()
    cp.parseBootAndExtClasspath(jreOption)
    cp.parseUserClasspath(cpOption)
    return cp
