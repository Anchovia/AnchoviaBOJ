import sys

def inputInteger():
    n = int(sys.stdin.readline())

    return n

def sumList(stack):
    result = 0

    for i in stack:
        result += i
    
    return result

def main():
    k = inputInteger()

    stack = []
    index = 0

    for i in range(0, k):
        number = inputInteger()
        
        try:
            if(number == 0):
                index -= 1

                del stack[index]
            
            else:
                index += 1

                stack.append(number)
        
        except IndexError:
            index += 1

    result = sumList(stack)

    print(result)

# __main__
main()