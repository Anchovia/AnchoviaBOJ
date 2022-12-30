import sys

def singleDataInput():
    data = int(sys.stdin.readline().strip())

    return data

def findSolution(rock):
    if(rock % 2 == 1):
        return 'SK'
    
    else:
        return 'CY'

def main():
    rock = singleDataInput()

    print(findSolution(rock))

main()