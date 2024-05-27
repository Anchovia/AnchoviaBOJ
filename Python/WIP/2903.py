def solution(n):
    if n == 1:
        return 9
    else:
        square = 1
        for _ in range(1, n):
            square *= 4
        point = square * 5 - square
    return point

def main():
    n = int(input())
    result = solution(n)
    print(result)

main()