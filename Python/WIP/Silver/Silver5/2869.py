from dataclasses import asdict
from re import L
import sys

def main():
    a, b, v = map(int, sys.stdin.readline().rstrip().split())

    up = a - b

    day = 0

    while 1:
        v -= up

        if v <= 0:
            break
        
        day += 1
    
    print(day)
    
main()