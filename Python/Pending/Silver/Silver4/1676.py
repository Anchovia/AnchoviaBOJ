import sys

def main():
    factorialResult = 1
    countZero = 0

    n = int(sys.stdin.readline())

    for i in range(1, n + 1):
        factorialResult *= i

    while(factorialResult % 10 == 0):
        factorialResult //= 10

        countZero += 1
    
    print(countZero)

# __main__
main()