import sys

def main():
    a, b = sys.stdin.readline().rstrip().split()

    a = "".join(reversed(a))
    b = "".join(reversed(b))

    numberList = [a, b]

    print(max(numberList))

# __main__
main()