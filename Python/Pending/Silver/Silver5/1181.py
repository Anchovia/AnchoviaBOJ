import sys

def main():
    strList = []
    lenList = []

    amount = int(sys.stdin.readline())

    for i in range(0, amount):
        data = sys.stdin.readline().rstrip()
        strList.append(data)
    
    strList = list(set(strList))

    strList.sort()

    for idx in range(0, len(strList)):
        lenList.append([len(strList[idx]), idx])

    lenList.sort(key=lambda x:x[0])

    for j in range(0, len(strList)):
        nowIdx = lenList[j][1]
        print(strList[nowIdx])

# __main__
main()