def main():
    x, y = map(int, input().split())

    if x > y:
        result = x + y
    else:
        result = y - x

    print(result)

main()