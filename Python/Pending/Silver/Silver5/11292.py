import sys

def makeDict(amountStudents):
    dictData = {}

    for _ in range(amountStudents):
        name, height = sys.stdin.readline().rstrip().split()
        dictData[name] = float(height)

    return dictData

def dictSort(dictData):
    dictData = dict(sorted(dictData.items(), key=lambda x: -x[1]))

    return dictData

def solution(dictData):
    listResult = list()

    dictSorted = dictSort(dictData)

    top = next(iter(dictSorted.values()))

    for key in dictSorted.keys():
        if top == dictSorted[key]:
            listResult.append(key)
        else:
            break
    
    strs = ""
    
    for i in range(len(listResult)):
        if (i == len(listResult) - 1):
            strs += listResult[i]
        else:
            strs += listResult[i] + " "

    print(strs)

def main():
    inputState = True

    while inputState:
        amountStudents = int(sys.stdin.readline())

        if amountStudents == 0:
            inputState = False
            return 0
        
        dictData = makeDict(amountStudents)
        solution(dictData)

main()