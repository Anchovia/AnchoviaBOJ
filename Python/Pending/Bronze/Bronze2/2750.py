def main():
    numberList = list()

    testCase = int(input())

    for _ in range(testCase):
        number = int(input())
        numberList.append(number)

    numberList.sort()

    strs = ""

    for i in numberList:
        strs += str(i) + "\n"

    print(strs, end="")

main()