import sys

def singleDataInput():
    data = int(sys.stdin.readline().strip())

    return data

def dataListInput():
    dataList = list(sys.stdin.readline().rstrip().split())

    return dataList

def caseInputFunc(testCase, userList):
    for i in range(testCase):
        dataList = dataListInput()

        dataDict = {'name':dataList[0], 'day':int(dataList[1]), 'month':int(dataList[2]), 'year':int(dataList[3])}
        userList.append(dataDict)
    
    return userList

def findBirthFunc(userList):
    maxYear = minYear = userList[0]['year']
    maxMonth = minMonth = userList[0]['month']
    maxDay = minDay = userList[0]['day']
    maxName = minName = userList[0]['name']

    for nowDict in userList:
        if(nowDict['year'] < maxYear):
            maxYear = nowDict['year']
            maxMonth = nowDict['month']
            maxDay = nowDict['day']
            maxName = nowDict['name']
        
        elif(nowDict['year'] == maxYear):
            if(nowDict['month'] < maxMonth):
                maxMonth = nowDict['month']
                maxDay = nowDict['day']
                maxName = nowDict['name']
            

            elif(nowDict['month'] == maxMonth):
                if(nowDict['day'] < maxDay):
                    maxDay = nowDict['day']
                    maxName = nowDict['name']
        
        elif(nowDict['year'] > minYear):
            minYear = nowDict['year']
            minMonth = nowDict['month']
            minDay = nowDict['day']
            minName = nowDict['name']
        
        elif(nowDict['year'] == minYear):
            if(nowDict['month'] > minMonth):
                minMonth = nowDict['month']
                minDay = nowDict['month']
                minName = nowDict['name']
            
            elif(nowDict['month'] == minMonth):
                if(nowDict['day'] > minDay):
                    minDay = nowDict['day']
                    minName = nowDict['name']

    return minName, maxName

def main():
    userList = []

    testCase = singleDataInput()
    
    userList = caseInputFunc(testCase, userList)

    minName, maxName = findBirthFunc(userList)

    print(minName)
    print(maxName)

#__main__
main()