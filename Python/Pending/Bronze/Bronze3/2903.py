import math

def solution(n):
    point = 4
    square = 1
    for i in range(n):
        square = 4 ** i
        point = int(point + square * 3 + math.sqrt(square) * 2)
    return point

def main():
    n = int(input())
    result = solution(n)
    print(result)

main()