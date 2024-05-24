def solution(number, n):
    result = []
    t = number // n
    print(t)

    return result

def main():
    number, n = map(int, input().split())
    result = solution(number, n)

main()