import sys

class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)

    def empty(self):
        if (len(self._data)) == 0:
            return False

        else:
            return True
    
    def top(self):
        return self._data[-1]

    def print(self):
        print(self._data)

def singleDataInput():
    data = int(sys.stdin.readline().strip())

    return data

def doubleDataInput():
    data1, data2 = map(int, sys.stdin.readline().rstrip().split())

    return data1, data2

def dataListInput():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

def trasferToData(dataList):
    M = dataList[0]
    N = dataList[1]
    K = dataList[2]

    return M, N, K

def makeIndexListFunc():
    indexList = Stack()

    dataList = dataListInput()
    M, N, K = trasferToData(dataList)

    for j in range(K):
        x, y = doubleDataInput()
        indexList.push([x, y])
    
    return indexList

def BFSFunc(nowIdx, indexList):
    removeList = []

    x = nowIdx[0]
    y = nowIdx[1]

    return removeList


def findWormFunc(indexList):
    result = 0

    while(indexList.empty()):
        nowIdx = indexList.pop()

        removeList = BFSFunc(nowIdx, indexList)

    return result

def __main__():
    testCase = singleDataInput()

    for i in range(testCase):
        indexList = makeIndexListFunc()

        result = findWormFunc(indexList)

        print(result)

__main__()