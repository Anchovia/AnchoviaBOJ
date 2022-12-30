import sys

class User:
    def __init__(self):
        self.name = None
        self.weight = None
        self.height = None
        self.rank = None
    
    def pushName(self, inputName):
        self.name = inputName
    
    def pushData(self, inputWeight, inputHeight):
        self.weight = inputWeight
        self.height = inputHeight
    
    def pushRank(self, inputRank):
        self.rank = inputRank

def singleIntegerInput():
    n = int(sys.stdin.readline())

    return n

def doubleIntegerInput():
    a, b = map(int, sys.stdin.readline().split())

    return a, b

def doComparison(bulkList):
    resultList = []

    return resultList

def main():
    bulkList = []

    n = singleIntegerInput()

    for i in range(1, n + 1):
        weight, height = doubleIntegerInput()
        bulkList.append([weight, height])
    
    resultList = doComparison(bulkList)


# __main__
main()