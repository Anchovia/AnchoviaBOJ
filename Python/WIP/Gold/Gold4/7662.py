import sys

def singleIntInput():
    n = int(sys.stdin.readline().rstrip())

    return n

def dataInput():
    data = sys.stdin.readline().rstrip()

    if(data.find(' ') == -1):
        a = data
        b = 0
    
    else:
        blankIndex = data.find(' ')

        a = data[:blankIndex]
        b = data[blankIndex + 1:]
    
    return a, int(b)

def i(q, n):
    q.append(n)

    return q

def d(q, n):
    try:
        if(n == 1):
            q.remove(max(q))
        
        else:
            q.remove(min(q))
    
    except ValueError:
        pass

    return q

def judgCmd(q, cmd, n):
    if(cmd == 'I'):
        q = i(q, n)
    
    else:
        q = d(q, n)

    return q

def main():
    t = singleIntInput()
    
    for i in range(0, t):
        q = []

        k = singleIntInput()

        for j in range(0, k):
            cmd, n = dataInput()

            q = judgCmd(q, cmd, n)
    
        if(len(q) == 0):
            print('EMPTY')
        
        else:
            maximum = max(q)
            minimum = min(q)

            print(maximum, minimum)

# __main__
main()