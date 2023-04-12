import math

def main():
    n, m = map(int, input().split(":"))
    lcm = math.lcm(n, m)

    print(f"{lcm // m}:{lcm // n}")

main()