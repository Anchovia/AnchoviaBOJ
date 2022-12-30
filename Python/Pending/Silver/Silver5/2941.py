# 단어 입력 함수
def wordInputFunc():
    strWord = input()

    return strWord

# 단어 체크 함수
def wordCheckFunc(strWord):
    nowIndex = 0
    result = 0

    while(nowIndex < len(strWord) - 1):
        nowWord = strWord[nowIndex]
        nextWord = strWord[nowIndex + 1]

        if(nowWord == 's' or nowWord == 'z'):
            if(nextWord == '='):
                nowIndex += 2
            
            else:
                nowIndex += 1
            
        elif(nowWord == 'c'):
            if(nextWord == '-'):
                nowIndex += 2
            
            elif(nextWord == '='):
                nowIndex += 2
            
            else:
                nowIndex += 1
            
        elif(nowWord == 'd'):
            if(nextWord == '-'):
                nowIndex += 2
             
            elif(nextWord == 'z'):
                try:
                    nextWord = strWord[nowIndex + 2]

                    if(nextWord == '='):
                        nowIndex += 3
                    
                    else:
                        nowIndex += 1
                
                except IndexError:
                    nowIndex += 1
            
            else:
                nowIndex += 1
        
        elif(nowWord == 'l' or nowWord == 'n'):
            if(nextWord == 'j'):
                nowIndex += 2
            
            else:
                nowIndex += 1
        
        else:
            nowIndex += 1

        result += 1

    if(nowIndex == len(strWord) - 1):
        result += 1

    else:
        pass
    
    return result


# 메인 함수
def main():
    strWord = wordInputFunc()

    result = wordCheckFunc(strWord)

    print(result)

# __main__
main()