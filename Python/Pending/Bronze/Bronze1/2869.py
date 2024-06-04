def main():
    a, b, v = map(int, input().split())
    result = 0
    if (v - a) // (a - b) == 0 and (v - a) % (a - b) != 0:
        result += 1
    else:
        result += (v - a) // (a - b)
        if (v - a) % (a - b) != 0:
            result += 1
    
    result += 1

    print(result)

main()