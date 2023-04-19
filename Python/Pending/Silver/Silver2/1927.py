import heapq
import sys

def main():
    heap = list()
    heapq.heapify(heap)

    dataSize = 0

    case = int(input())

    for _ in range(case):
        n = int(sys.stdin.readline())

        if n == 0:
            if dataSize == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
                dataSize -= 1
        else:
            heapq.heappush(heap, n)
            dataSize += 1

main()