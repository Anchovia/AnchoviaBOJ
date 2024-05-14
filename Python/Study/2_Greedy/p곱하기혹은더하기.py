def solution(numberList):
    solutionStr = ""

    for i in range(len(numberList)):
        nowNumber = numberList[i]

        if i == len(numberList) - 1:
            solutionStr += nowNumber
            return eval(solutionStr)
        
        nextNumber = numberList[i + 1]

        if nowNumber == "0" or nowNumber == "1" or nextNumber == "0" or nextNumber == "1":
            solutionStr += nowNumber
            solutionStr += "+"
        else:
            solutionStr += nowNumber
            solutionStr += "*"

def __main__():
    numberList = input()
    result = solution(list(numberList))
    print(result)

__main__()