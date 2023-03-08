s = "567"

numberList = list(s)

result = int(numberList[0])

for i in range(1, len(numberList)):
    if(result < 1 or int(numberList[i]) < 1):
        result += int(numberList[i])
    
    else:
        result *= int(numberList[i])

print(result)