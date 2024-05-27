import sys


def solution(a, b):
    if a % b == 0 or b % a == 0:
        if a <= b:
            print("factor")
        else:
            print("multiple")
    else:
        print("neither")

def main():
    while True:
        a, b = map(int, sys.stdin.readline().strip(). split())
        if [a, b] == [0, 0]:
            break
        else:
            solution(a, b)

main()