import sys

def main():
    count = 0

    x = int(sys.stdin.readline())

    while(x != 1):
        print(x)
        
        if(x % 3 == 0):
            x //= 3
            count += 1
        
        elif(x % 2 == 0):
            x //= 2
            count += 1
        
        else:
            x -= 1
            count += 1
    
    print(count)

# __main__
main()