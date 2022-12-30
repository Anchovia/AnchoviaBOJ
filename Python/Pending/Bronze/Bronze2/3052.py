import sys

def main():
    resultList = []

    for i in range(0, 10):
        n = int(sys.stdin.readline().rstrip())
        
        resultList.append(n % 42)
    
    resultList = list(set(resultList))
    print(len(resultList))

# __main__
main()