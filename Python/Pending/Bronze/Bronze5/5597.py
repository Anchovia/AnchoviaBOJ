def main():
    indexList = [0] * 31

    for _ in range(28):
        data = int(input())
        
        indexList[data] += 1

    for index in range(1, 31, 1):
        if indexList[index] == 0:
            print(index)

main()