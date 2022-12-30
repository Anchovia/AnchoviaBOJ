data = input()

blank_index = data.find(' ')

n = int(data[:blank_index])
m = int(data[blank_index + 1:])

result = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        result += 1

print(result - 1)