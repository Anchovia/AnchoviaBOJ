def main():
    school = int(input())
    pc = int(input())
    aca = int(input())
    home = int(input())

    sum = school + pc + aca + home

    min = sum // 60
    sum -= min * 60

    print(min)
    print(sum)

main()