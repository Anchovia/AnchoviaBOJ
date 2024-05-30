def solution(a, b, c, d, e, f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                return x, y

def main():
    a, b, c, d, e, f = map(int, input().split())
    x, y = solution(a, b, c, d, e, f)
    print(x, y)

main()