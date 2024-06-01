from math import sqrt

def isPrime(k):
    end = int(sqrt(k))
    for i in range(2, end + 1):
        if k % i == 0:
            return False
        
    return True

def solution(n):
    count = 0
    for k in range(n + 1, 2 * n + 1):
        if k == 1:
            pass

        if isPrime(k):
            count += 1

    return count

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        result = solution(n)
        print(result)

main()