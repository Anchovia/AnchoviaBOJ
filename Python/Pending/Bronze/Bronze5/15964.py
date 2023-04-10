def solution(a, b):
    result = 0

    result = (a + b) * (a - b)

    return result

def main():
    a, b = map(int, input().split())

    result = solution(a, b)

    print(result)

main()