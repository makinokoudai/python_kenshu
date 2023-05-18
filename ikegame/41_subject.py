import sys
args = [int(sys.argv[i]) for i in [1,2,3]]

def main(args):
    #条件1
    if args[0] < 50:
        return False
    if args[1] < 50:
        return False
    if args[2] < 50:
        return False
    
    #条件1
    if args[0] >= 70 and args[1] >= 70 and args[2] >= 70:
        return True

    elif args[0] + args[1] + args[2] >= 220:
        return True
    
    return False

if main(args):
    print("合格",end="")
else:
    print("不合格",end="")