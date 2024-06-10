def makeFizz(i):
    if i % 3 == i % 5 == 0:
        return "FizzBuzz"
    elif  i % 3 == 0 and i % 5 != 0:
        return "Fizz"
    elif i % 3 != 0 and i % 5 == 0:
        return "Buzz"
    else:
        return i

def main():
    dataList = [input() for _ in range(3)]
    for idx, now in enumerate(dataList):
        if now.isdigit():
            now = int(now)
            if idx == 0:
                result = makeFizz(now + 3)
            elif idx == 1:
                result = makeFizz(now + 2)
            else:
                result = makeFizz(now + 1)
            break
    print(result)

main()