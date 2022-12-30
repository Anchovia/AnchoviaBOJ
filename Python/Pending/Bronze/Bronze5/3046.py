data = input()

blank_index = data.find(' ')

r1 = int(data[:blank_index])
s = int(data[blank_index + 1:])

result = 2 * s - r1

print(result)