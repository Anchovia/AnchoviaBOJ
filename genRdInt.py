import random

def isSame(numberStack):
    count = 0
    needCheckNumber = numberStack[len(numberStack) - 1]
    for i in range(len(numberStack)):
        if numberStack[i] == needCheckNumber:
            count += 1
    if count > 1:
        return True

def isContinuous(sortedStack):
    new = True
    count = 0
    for nowData in sortedStack:
        if count >= 3:
            return True
        
        if new:
            pastData = nowData
            new = False
        else:
            if nowData == pastData + 1:
                count += 1
                pastData = nowData
    return False

def isGroup(sortedStack):
    boundary = [8, 15, 22, 29, 36, 43]
    group = [0 for _ in range(len(boundary) + 1)]

    for nowData in sortedStack:
        for i, nowBound in enumerate(boundary):
            if nowData < nowBound:
                group[i] += 1
                break
        else:
            group[-1] += 1
    
    for nowGroupData in group:
        if nowGroupData >= 4:
            return True

def judgFunc(numberStack):
    if isSame(numberStack):
        return False
    
    sortedStack = sorted(numberStack)
    if isContinuous(sortedStack):
        return False
    
    if isGroup(sortedStack):
        return False
        
    return True

def genData():
    count = 2
    numberStack = [random.randint(1, 45) for _ in range(2)]
    while count != 7:
        judg = judgFunc(numberStack)
        if judg:
            numberStack.sort()
            numberStack.append(random.randint(1, 45))
            count += 1
        else:
            numberStack.pop()
            count -= 1
    numberStack.pop()
    return numberStack

def main():
    resultStack = genData()
    print(resultStack)

# 코드 실행
main()