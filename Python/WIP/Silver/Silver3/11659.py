from collections import deque

def main():
    numberAmount, tryAmount = map(int, input().split())

    numberList = [0] * 1001

    dataList = deque(map(int, input().split()))

    for _ in range(numberAmount):
        number = dataList.popleft()

        numberList[number] += number
    
    for _ in range(tryAmount):
        startIdx, endIdx = map(int, input().split())

        print(sum(numberList[startIdx:endIdx + 1]))

main()