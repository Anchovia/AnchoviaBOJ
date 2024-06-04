from collections import deque

def solution(sentence):
    resultDeque = deque([])
    while True:
        now = sentence.popleft()
        if now == '.':
            break
        else:
            if now == '(' or now == '[':
                resultDeque.append(now)
            elif now == ')' or now == ']':
                if len(resultDeque) == 0:
                    return "no"
                else:
                    check = resultDeque.pop()
                    if check == '[':
                        if now != ']':
                            return "no"
                    elif check == '(':
                        if now != ')':
                            return "no"
    if len(resultDeque) == 0:
        return "yes"
    else:
        return "no"

def main():
    while True:
        sentence = deque(input())
        if len(sentence[0]) == 1 and sentence[0] == '.':
            break
        else:
            result = solution(sentence)
            print(result)

main()