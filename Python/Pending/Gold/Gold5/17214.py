def makePolynomialList():
    polynomialList = list()
    rawPolynomial = ""
    
    polynomial = input()

    for i in range(len(polynomial)):
        nowStr = polynomial[i]

        if i != 0 and nowStr == "+" or nowStr == "-":
            if len(rawPolynomial) > 0:
                polynomialList.append(rawPolynomial)
            rawPolynomial = ""

        rawPolynomial += nowStr
    
    polynomialList.append(rawPolynomial)
    
    return polynomialList

def solution(polynomialList):
    resultPolynomialStr = ""

    for nowPolynomial in polynomialList:
        numberStrs = ""
        xStrs = ""
        symbolStrs = ""

        for nowStr in nowPolynomial:
            if nowStr == "x":
                xStrs += nowStr
            elif nowStr == "-" or nowStr == "+":
                symbolStrs += nowStr
            else:
                numberStrs += nowStr

        if len(symbolStrs) < 1:
            symbolStrs += "+"
        
        if len(xStrs) > 0:
            integrationNumber = int(numberStrs) // 2

            if integrationNumber == 1:
                resultPolynomialStr += symbolStrs + xStrs + xStrs
            else:
                resultPolynomialStr += symbolStrs + str(integrationNumber) + xStrs + xStrs
        else:
            if numberStrs == "0":
                break
            elif numberStrs == "1":
                resultPolynomialStr += symbolStrs + "x"
            else:
                resultPolynomialStr += symbolStrs + numberStrs + "x"

    resultPolynomialStr += "+W"
    
    if resultPolynomialStr[0] == "+":
        newResultStr = ""

        for i in range(1, len(resultPolynomialStr)):
            newResultStr += resultPolynomialStr[i]
        
        resultPolynomialStr = newResultStr
    
    return resultPolynomialStr

def main():
    polynomialList = makePolynomialList()
    resultPolynomialList = solution(polynomialList)

    print(resultPolynomialList)

main()