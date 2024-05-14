def solution(n, k):
    count = 0

    while True:
        if n < k:
            break

        if n % k != 0:
            target = (n // k) * k
            count += n - target
            n = target

        n //= k
        count += 1
    
    count += n - 1

    return count

def __main__():
    n, k = map(int, input().split())
    count = solution(n, k)
    print(count)

__main__()
