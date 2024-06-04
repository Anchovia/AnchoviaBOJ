def solution(a1, a0, c, n0):
    for n in range(n0, 101):
        if (a1 * n + a0) <= c * n:
            pass
        else:
            return 0
    return 1

def main():
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    result = solution(a1, a0, c, n0)
    print(result)

main()