from sys import stdin

def main():
    n = int(stdin.readline())
    sums = 0
    numIdx = [0 for i in range(-4000, 4001)]
    max = -4000
    min = 4000

    for _ in range(n):
        # 입력
        num = int(stdin.readline())
        
        numIdx[num] += 1

        # 최대 최소
        if num > max:
            max = num
        if num < min:
            min = num

        # 평균
        sums += num
    
    mostMax = 0
    for now in numIdx:
        if now > mostMax:
            mostMax = now
    
    mostList = []
    for idx, now in enumerate(numIdx):
        idx += 1
        if len(mostList) == 2:
            break
        if now == mostMax:
            mostList.append(idx)
    
    # 평균
    print(round(sums / n))
    # 중앙
    print("중앙")
    # 최빈
    if len(mostList) > 1:
        print(mostList[1])
    else:
        print(mostList[0])
    # 범위
    print(max - min)

main()