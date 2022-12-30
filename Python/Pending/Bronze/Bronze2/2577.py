import sys

def main():
    number = 1
    idxList = [0] * 10

    for i in range(0, 3):
        n = int(sys.stdin.readline().rstrip())

        number *= n

    for j in str(number):
        for k in range(0, 10):
            if j == str(k):
                idxList[k] += 1
    
    for m in idxList:
        print(m)

# __main__
main()