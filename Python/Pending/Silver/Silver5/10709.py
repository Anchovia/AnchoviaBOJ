def makeCloudList(height):
    cloudList = list()

    for _ in range(height):
        dataList = input()

        cloudList.append(dataList)

    return cloudList

def solution(cloudList):
    matrixList = list()

    for nowStrs in cloudList:
        rawMatrixList = list()

        matrixCount = -1
        cloudJudg = False

        for nowStr in nowStrs:
            if cloudJudg:
                matrixCount += 1

            if nowStr == "c":
                cloudJudg = True
                matrixCount = 0

            rawMatrixList.append(matrixCount)
        
        matrixList.append(rawMatrixList)
    
    return matrixList


def main():
    height, width = map(int, input().split())

    cloudList = makeCloudList(height)

    matrixList = solution(cloudList)

    for nowMatrix in matrixList:
        print(" ".join(str(data) for data in nowMatrix))

main()