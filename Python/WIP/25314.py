def main():
    strs = ""

    n = int(input())

    result = int(n / 4)

    for _ in range(result):
        strs += "long "
    
    print(strs + "int")

main()