import sys

def main():
    case = int(sys.stdin.readline().rstrip())

    for i in range(0, case):
        resultStrData = ""
        
        run, strData = sys.stdin.readline().rstrip().split()

        for j in strData:
            resultStrData += j * int(run)
        
        print(resultStrData)

# __main__
main()