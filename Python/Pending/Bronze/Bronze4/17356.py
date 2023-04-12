def main():
    a, b = map(int, input().split())

    m = (b - a) / 400

    result = 1 / (1 + 10 ** m)

    print(result)

main()