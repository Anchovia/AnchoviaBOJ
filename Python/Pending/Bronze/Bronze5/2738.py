def makeMatrix(m):
    matrixA = list()
    matrixB = list()

    for _ in range(m):
        data = list(map(int, input().split()))
        matrixA.append(data)
    
    for _ in range(m):
        data = list(map(int, input().split()))
        matrixB.append(data)

    return matrixA, matrixB

def sumMatrix(m, n, matrixA, matrixB):
    resultMatrix = list()

    for x in range(m):
        newDataList = list()

        for y in range(n):
            newData = matrixA[x][y] + matrixB[x][y]

            newDataList.append(newData)
        
        resultMatrix.append(newDataList)

    return resultMatrix

def printMatrix(resultMatrix):
    for data in resultMatrix:
        print(' '.join(map(str, data)))

def main():
    m, n = map(int, input().split())

    matrixA, matrixB = makeMatrix(m)
    resultMatrix = sumMatrix(m, n, matrixA, matrixB)

    printMatrix(resultMatrix)

main()