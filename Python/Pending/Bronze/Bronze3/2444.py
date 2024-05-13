def solution(n):
    blank = n
    star = 1
    for i in range(2 * n + 1):
        if i < n:
            print(' ' * blank + '*' * star)
            blank -= 1
            star += 2
        elif i == n:
            print('*' * star)
        else:
            blank += 1
            star -= 2
            print(' ' * blank + '*' * star)

def main():
    n = int(input())
    if n == 1:
        print('*')
    else:
        solution(n - 1)

main()