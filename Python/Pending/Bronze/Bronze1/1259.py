import sys

def singleIntInput():
    n = int(sys.stdin.readline().rstrip())

    return n

def singleStrInput():
    s = sys.stdin.readline().rstrip()

    return s

def main():
    s = ''

    while True:
        frontList = []
        backList = []

        s = singleStrInput()

        if(s != '0'):
            for i in range(0, len(s)):
                frontList.append(s[i])
            
            for j in range(len(s) - 1, -1, -1):
                backList.append(s[j])

            if(frontList == backList):
                print("yes")
            
            else:
                print("no")
            
        else:
            break

# __main__
main()