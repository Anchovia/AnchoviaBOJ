import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    print(n // m)
    print(n % m)

# __main__
main()