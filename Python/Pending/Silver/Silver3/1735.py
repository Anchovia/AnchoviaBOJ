import math

def solution(a, b, c, d):
    lcm = math.lcm(b, d)
    i = a * lcm // b + c * lcm // d
    gcd = math.gcd(i, lcm)
    if i // gcd != 0:
        i //= gcd
        lcm //= gcd
    return i, lcm

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    i, j = solution(a, b, c, d)
    print(f"{i} {j}")

main()