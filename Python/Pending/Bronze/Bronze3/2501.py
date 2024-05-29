def judgFunc(i, n):
    if n % i == 0: return i

def solution(n, k):
    primeNumList = [judgFunc(i, n) for i in range(1, n + 1) if judgFunc(i, n) is not None]
    length = len(primeNumList)
    if length < k:
        return 0
    else:
        return primeNumList[k - 1]
    

def main():
    n, k = map(int, input().split())
    result = solution(n, k)
    print(result)

main()