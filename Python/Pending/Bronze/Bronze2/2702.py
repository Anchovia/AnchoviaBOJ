import math

def main():
    testCase = int(input())

    for _ in range(testCase):
        a, b = map(int, input().split())
        print(f"{math.lcm(a, b)} {math.gcd(a, b)}")

main()