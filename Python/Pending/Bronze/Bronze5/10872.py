def factorial(n):
    result = 1

    if n == 0:
        return 1
    else:
        for i in range(n, 0, -1):
            result *= i

        return result


def main():
    n = int(input())

    result = factorial(n)

    print(result)

main()