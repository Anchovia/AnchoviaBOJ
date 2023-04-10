def makeMatrix(n, m):
    matrixA = list()
    matrixB = list()

    for _ in range(n):
        data = list(map(int, input().split()))
        matrixA.append(data)
    
    for _ in range(m):
        data = list(map(int, input().split()))
        matrixB.append(data)

    return matrixA, matrixB

def sumMatrix(n, m, matrixA, matrixB):
    resultMatrix = list()

    for i in range(n):
        newDataList = list()

        for j in range(m):
            newData = matrixA[i][j] + matrixB[i][j]

            newDataList.append(newData)
        
        resultMatrix.append(newDataList)

    return resultMatrix

def printMatrix(resultMatrix):
    for data in resultMatrix:
        print(' '.join(map(str, data)))

def main():
    n, m = map(int, input().split())

    matrixA, matrixB = makeMatrix(n, m)
    resultMatrix = sumMatrix(n, m, matrixA, matrixB)

    printMatrix(resultMatrix)

main()