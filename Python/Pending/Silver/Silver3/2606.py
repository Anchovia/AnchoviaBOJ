import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().strip())

    return data

def dataListInputFunc():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

def findNetWork(linkList):
    networkList = [linkList[len(linkList) - 1]]
    del linkList[len(linkList) - 1]

    while(len(linkList) != 0):
        judg = True

        for nowIdx in range(len(linkList) - 1, -1, -1):
            nowList = linkList[nowIdx]

            for i in range(0, len(networkList)):
                if(list(set(nowList) & set(networkList[i])) != []):
                    networkList[i] += nowList
                    networkList[i] = set(networkList[i])
                    networkList[i] = list(networkList[i])

                    del linkList[nowIdx]
                    nowIdx -= 1

                    judg = False
        
        if(judg):
            networkList.append(linkList[len(linkList) - 1])
            del linkList[len(linkList) - 1]
   
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
        linkList = []

        for i in range(groupCase):
            dataList = dataListInputFunc()
            linkList.append(dataList)

        print(findResult(findNetWork(linkList)))

# __main__
main()
