def solution(data):
    result = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    
    return result
    
def __main__():
    data = input()
    result = solution(data)
    print(result)

__main__()