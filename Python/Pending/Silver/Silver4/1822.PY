def main():
    amountA, amountB = map(int, input().split())

    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))

    resultSet = list(setA - setB)
    resultSet.sort()
    resultLen = len(resultSet)

    print(resultLen)

    strs = ""

    if resultLen > 0:
        print(" ".join(str(i) for i in resultSet))

main()