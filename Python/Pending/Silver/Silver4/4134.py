import math

def main():
    testCase = int(input())

    for _ in range(testCase):
        n = int(input())
        result = solution(n)
        print(result)

def solution(n):
    k = n
    while True:
        if k == 0 or k == 1:
            k = 2

        if findPrine(k):
            k += 1
        else:
            return k

def findPrine(n):
    end = int(math.sqrt(n))
    for i in range(2, end + 1):
        if n % i == 0:
            return True
        else:
            False
main()