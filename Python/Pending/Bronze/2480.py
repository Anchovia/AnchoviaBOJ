def main():
    a, b, c = map(int, input().split())

    result = 0

    if a == b == c:
        result = 10000 + a * 1000
    elif a == b or b == c or c == a:
        if a == b:
            result = 1000 + a * 100
        elif b == c:
            result = 1000 + b * 100
        else:
            result = 1000 + c * 100
    else:
        numList = [a, b, c]
        numList.sort()

        result = numList[2] * 100
    
    print(result)

main()