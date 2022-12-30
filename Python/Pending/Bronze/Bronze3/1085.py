import sys

def fourIntegerInput():
    a, b, c, d = map(int, sys.stdin.readline().split())

    return a, b, c, d

def calculLength(x, y, w, h):
    if(x <= w - x):
        resultX = x
    
    else:
        resultX = w - x
    
    if(y <= h - y):
        resultY = y
    
    else:
        resultY = h - y
    
    if(resultX <= resultY):
        return resultX
    
    else:
        return resultY

def main():
    x, y, w, h = fourIntegerInput()

    result = calculLength(x, y, w, h)

    print(result)

# __main__
main()