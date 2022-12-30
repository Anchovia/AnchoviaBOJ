sum = 0

for i in range(0, 5, 1):
    data = int(input())

    if(data < 40):
        data = 40

    sum += data

print(int(sum/5))