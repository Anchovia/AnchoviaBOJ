def solution(n):
    pivot = 2
    result = 1
    sum = 6
    while True:
        if n < pivot:
            return result
        else:
            pivot += sum
            sum += 6
            result += 1

def main():
    n = int(input())
    result = solution(n)
    print(result)

main()