def solution(wordsMatrix):
    maxLen = 0
    sentence = ""
    
    for nowDatas in wordsMatrix:
        if maxLen < len(nowDatas):
            maxLen = len(nowDatas)

    for i in range(maxLen):
        for j in range(5):
            if len(wordsMatrix[j]) > i:
                sentence += wordsMatrix[j][i]
            else:
                pass
    
    print(sentence)

def main():
    wordsMatrix = [list(input()) for _ in range(5)]

    solution(wordsMatrix)

main()