# 단어 갯수 입력 함수
def wordNumberInputFunc(n):
    n = int(input())

    return n

# 단어 입력 함수
def wordInputFunc(wordList, n):
    for i in range(1, n + 1):
        word = input()
        wordList.append(word)
    
    return wordList

# 그룹 체크 함수
def groupCheckFunc(wordList, n):
    for word in wordList:
        index = 0

        pastLetter = word[0]
        groupList = []

        for nowLetter in word:
            if(nowLetter in groupList and nowLetter == pastLetter):
                index += 1
            
            elif(nowLetter in groupList):
                n -= 1
                break
            
            else:
                groupList.append(nowLetter)
                index += 1
            
            pastLetter = word[index - 1]
        
    return n

# 메인 함수
def main():
    n = 0
    wordList = []

    n = wordNumberInputFunc(n)
    wordList = wordInputFunc(wordList, n)

    result = groupCheckFunc(wordList, n)

    print(result)

# __main__
main()