import sys

def binarySearch(arr, data):
    frontIdx = 0
    lastIdx = len(arr) - 1
    midIdx = len(arr) // 2

    while(data != arr[midIdx]):
        if(data < arr[midIdx]):
            lastIdx = midIdx - 1
        
        elif(data > arr[midIdx]):
            frontIdx = midIdx + 1

        midIdx = (lastIdx - frontIdx) // 2 + frontIdx

    return midIdx

def main():
    arr = [1, 3, 5, 7, 9, 11, 13]

    data = int(sys.stdin.readline().rstrip())

    result = binarySearch(arr, data)

    print(result)

# __main__
main()

