import sys

def main():
    run = int(sys.stdin.readline().rstrip())

    for i in range(0, run):
        bonus = 1
        result = 0

        strData = sys.stdin.readline().rstrip()

        for j in strData:
            if(j == 'O'):
                result += bonus
                bonus += 1
            
            else:
                bonus = 1
        
        print(result)
    
# __main__
main()