import sys

def main():
    n = int(sys.stdin.readline().rstrip())

    b = format(n, 'b')
    rb = ''.join(reversed(b))

    result = int(rb, 2)

    print(result)

# __main__
main()