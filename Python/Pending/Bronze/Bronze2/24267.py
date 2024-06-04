def solution(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    elif n == 4:
        return 4
    else:
        result = 4
        sums = 3
        for i in range(0, n - 4):
            sums += 3 + i
            result += sums

    return result

def main():
    n = int(input())
    result = solution(n)
    print(result)
    print(3)

main()