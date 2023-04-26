from collections import deque
import math

def main():
    rings = int(input())

    ringList = list(map(int, input().split()))

    ringQueue = deque(ringList)

    targetRing = ringQueue.popleft()

    for nowRing in ringQueue:
        if targetRing % nowRing == 0:
            print(f"{targetRing // nowRing}/{1}")
        else:
            print(f"{targetRing // math.gcd(targetRing, nowRing)}/{nowRing // math.gcd(targetRing, nowRing)}")

main()