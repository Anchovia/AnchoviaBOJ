import sys
import heapq

def main():
    dataSize = 0
    heap = list()
    heapq.heapify(heap)

    case = int(input())

    for _ in range(case):
        data = int(sys.stdin.readline())

        if data == 0:
            if dataSize == 0:
                print(0)
            else:
                print(heapq.heappop(heap) * -1)
                dataSize -= 1
        else:
            heapq.heappush(heap, data * -1)
            dataSize += 1

main()