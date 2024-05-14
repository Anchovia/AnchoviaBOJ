def main():
    count = 0

    number, target = input().split()

    number = int(number)
    target = str(target)

    for i in range(1, number + 1):
        i = str(i)
        strList = list(i)

        for nowStr in strList:
            if(nowStr == target):
                count += 1
    
    print(count)

# __main__
main()