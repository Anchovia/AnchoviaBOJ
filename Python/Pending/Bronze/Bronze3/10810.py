def main():
    size, testCase = map(int, input().split()) 
    dataList = [0] * (size + 1)

    for _ in range(testCase):
        start, end, ball = map(int, input().split())

        for i in range(start, end + 1):
            dataList[i] = ball
    
    dataList.pop(0)

    print(" ".join(str(i) for i in dataList))

main()