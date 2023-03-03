# module import
import sys

def main():
    n = int(input())

    dataList = map(int, sys.stdin.readline().rstrip().split())

    dataList = set(dataList)
    
    numberList = list(dataList)
    numberList.sort()
    
    print(*numberList)

# __main__
main()