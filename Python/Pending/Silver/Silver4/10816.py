dataList = [0] * 20000001

n = int(input())
card = list(map(int, input().split()))
m = int(input())
solve = list(map(int, input().split()))

solution = list()

for i in card:
    dataList[i] += 1

for j in solve:
    solution.append(dataList[j])

print(*solution, sep=' ')