from math import sqrt

def isNotPrime(k):
    end = int(sqrt(k))
    for i in range(2, end + 1):
        if k % i == 0:
            return False
        
    return True

def solution(n, m):
    if n == 1:
        n = 2
        
    for k in range(n, m + 1):
        if isNotPrime(k):
            print(k)

def main():
    n, m = map(int, input().split())
    solution(n, m)

main()