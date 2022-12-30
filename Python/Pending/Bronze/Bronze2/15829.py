import sys

def calculForHashing(l, strData):
    strDataSum = 0
    count = 0

    for i in strData:
        strDataSum += int(ord(i) - 96) * (31 ** count)

        count += 1

    h = strDataSum % 1234567891

    return h

def main():
    l = int(sys.stdin.readline().rstrip())
    strData = sys.stdin.readline().rstrip()

    h = calculForHashing(l, strData)

    print(h)

# __main__
main()