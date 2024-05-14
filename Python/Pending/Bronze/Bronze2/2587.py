def main():
    numberList = [int(input()) for _ in range(5)]
    numberList.sort()
    print(int(sum(numberList) / 5))
    print(numberList[2])

main()
