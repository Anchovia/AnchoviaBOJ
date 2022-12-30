import sys

def main():
    wordList = [0] * 26

    strData = sys.stdin.readline().rstrip()

    for i in strData:
        for j in range(0, 26):
            if(j == ord(i.lower()) - 97):
                wordList[j] += 1

    maxCount = 0

    maxData = max(wordList)

    for k in wordList:
        if(k == maxData):
            maxCount += 1
    
    if(maxCount == 1):
        print(chr(wordList.index(maxData) + 65))
    
    else:
        print("?")
    
main()