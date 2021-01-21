import argparse
import classpath

__version__ = "0.0.1"
__author__ = "shiyi.liu"

def startJVM(args):
    cp = classpath.Parse(args.Xjre, args.classpath)
    print(f"classpath:{cp}, class{args.Class}, args: {args}")
    className = args.Class.replace(".","/")
    classData, _, err = cp.ReadClass(className)
    if err != None:
        print(f"Could not find or load main class {args.Class}")
        return
    print(f"classdata:{classData}")

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
