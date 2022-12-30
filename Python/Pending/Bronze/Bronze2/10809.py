import sys

def main():
    wordList = [-1] * 26
    idx = 0

    strData = sys.stdin.readline().rstrip()

    for i in strData:
        for j in range(0, 26):
            if(j == ord(i) - 97):
                if wordList[j] == -1:
                    wordList[j] = idx
                
                else:
                    pass
    
        idx += 1
    
    for k in range(0, len(wordList) - 1):
        print(wordList[k], end = " ")

    print(wordList[len(wordList) - 1])
    
# __main__
main()