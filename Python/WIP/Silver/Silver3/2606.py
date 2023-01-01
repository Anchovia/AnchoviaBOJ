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
    
    def sorter(self):
        self._data.sort()

def singleDataInputFunc():
    data = int(sys.stdin.readline().strip())

    return data

def dataListInputFunc():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

def findNetWork(linkList):
    networkList = [linkList.pop()]

    while(linkList.empty()):
        nowList = linkList.pop()
        judg = True

        for i in range(0, len(networkList)):
            if(list(set(nowList) & set(networkList[i])) != []):
                networkList[i] = networkList[i] + nowList
                networkList[i] = set(networkList[i])
                networkList[i] = list(networkList[i])
                judg = False
                break

        if(judg):
            networkList.append(nowList)
        
    return networkList

def findResult(networkList):
    for nowList in networkList:
        if(1 in nowList):
            return len(nowList) - 1
    
    return 0
                
def main():
    computerCase = singleDataInputFunc()
    groupCase = singleDataInputFunc()

    if(groupCase == 0):
        print(0)

        return 0
    
    else:
        linkList = Stack()

        for i in range(groupCase):
            dataList = dataListInputFunc()
            dataList.sort()
            linkList.push(dataList)

        linkList.sorter()
        networkList = findNetWork(linkList)

        print(networkList)
        print(findResult(networkList))

# __main__
main()
