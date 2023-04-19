def solution(polynomialList):
    resultStr = ""

    for nowPolynomial in polynomialList:
        xCount = 0

        for nowStr in nowPolynomial:
            if nowStr == "x":
                xCount += 1
        
        if xCount > 0:
            if nowPolynomial[0] == "x":
                resultStr += ("1")
            elif nowPolynomial[0] == "+" and nowPolynomial[1] == "x":
                resultStr += ("+1")
            elif nowPolynomial[0] == "-" and nowPolynomial[1] == "x":
                resultStr += ("-1")
            else:
                newStr = ""

                for nowStr in nowPolynomial:
                    if nowStr == "x":
                        resultStr += (newStr)
                        break

                    newStr += nowStr
        else:
            pass

    newResultStr = ""


    if len(resultStr) > 0 and resultStr[0] == "+":
        for i in range(1, len(resultStr)):
            newResultStr += resultStr[i]

            resultStr = newResultStr

    return resultStr

def makeDataList(polynomial):
    polynomialList = list()
    newPolynomial = ""

    for i in range(len(polynomial)):
        if i != 0 and polynomial[i] == "-" or polynomial[i] == "+":
            polynomialList.append(newPolynomial)
            newPolynomial = ""

        newPolynomial += polynomial[i]
    
    polynomialList.append(newPolynomial)
    
    return polynomialList

def main():
    polynomial = input()

    polynomialList = makeDataList(polynomial)

    resultStr = solution(polynomialList)

    if len(resultStr) == 0:
        print(0)
    else:
        print(resultStr)

main()