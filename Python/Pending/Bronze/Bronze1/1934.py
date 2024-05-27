import math
import sys

def solution(a, b):
    lcm = math.lcm(a, b)
    return lcm

def main():
    testCase = int(input())
    for _ in range(testCase):
        a, b = map(int, sys.stdin.readline().strip().split())
        lcm = solution(a, b)
        print(lcm)

main()