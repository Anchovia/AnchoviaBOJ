def main():
    a, b, c = map(int, input().split())

    if b % 4 == 1:
        b = 1
    elif b % 4 == 2:
        b = 2
    elif b % 4 == 3:
        b = 3
    else:
        b = 4

    print((a ** b) % c)

main()