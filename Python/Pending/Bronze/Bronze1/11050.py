import sys

def doubleIntInput():
    n, k = map(int, sys.stdin.readline().rstrip().split())

    return n, k

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def main():
    n, k = doubleIntInput()

    result = int(factorial(n) / (factorial(k) * (factorial(n - k))))

    print(result)

main()