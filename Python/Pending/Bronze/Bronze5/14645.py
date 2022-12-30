def doubleIntegerInput():
    a, b = map(int, input().split())

    return a, b

def main():
    n, k = doubleIntegerInput()

    for i in range(0, n):
        a, b = doubleIntegerInput()

    print("비와이")

# __main__
main()