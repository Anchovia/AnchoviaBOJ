import sys

def main():
    result = 0

    run = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()

    for i in data:
        result += int(i)
    
    print(result)

# __main__
main()