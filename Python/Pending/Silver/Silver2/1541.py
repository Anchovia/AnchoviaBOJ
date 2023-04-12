def solution(dataList):
    splitList = dataList.split("-")
    fistData = eval(splitList.pop(0))

    for i in splitList:
        fistData -= eval(i)

    return fistData

def setStr(formula):
    symbolList = list()

    newFormula = ""
    newNumberList = list()

    for i in formula:
        if i == "+" or i == "-":
            symbolList.append(i)
    
    formula = formula.replace("+", ".").replace("-", ".")
    numberList = formula.split(".")

    for j in numberList:
        j = int(j)
        j = str(j)

        newNumberList.append(j)

    for k in range(len(symbolList)):
        newFormula += newNumberList[k] + symbolList[k]
    
    newFormula += newNumberList[len(newNumberList) - 1]

    return newFormula

def main():
    formula = input()
    dataList = setStr(formula)

    min = solution(dataList)

    print(min)

main()