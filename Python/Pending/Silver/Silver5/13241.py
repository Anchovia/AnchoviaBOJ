import math

def main():
    a, b = map(int, input().split())

    lcm = math.lcm(a, b)

    print(lcm)

# __main__
main()