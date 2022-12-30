import sys

def singleIntegerInput():
    a = int(sys.stdin.readline())

    return a

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

def push_front(deck, x):
    deck.insert(0, x)

    return deck

def push_back(deck, x):
    deck.append(x)

    return deck

def pop_front(deck):
    if(len(deck) == 0):
        print(-1)

    else:
        print(deck[0])
        del deck[0]
    
    return deck

def pop_back(deck):
    if(len(deck) == 0):
        print(-1)

    else:
        print(deck[len(deck) - 1])
        del deck[len(deck) - 1]
    
    return deck

def size(deck):
    print(len(deck))

def empty(deck):
    if(len(deck) == 0):
        print(1)
    
    else:
        print(0)

def front(deck):
    if(len(deck) == 0):
        print(-1)
    
    else:
        print(deck[0])

def back(deck):
    if(len(deck) == 0):
        print(-1)
    
    else:
        print(deck[len(deck) - 1])

def judgeCommend(deck, command, data):
    if(command == 'push_front'):
        deck = push_front(deck, data)
    
    elif(command == 'push_back'):
        deck = push_back(deck, data)

    elif(command == 'pop_front'):
        deck = pop_front(deck)

    elif(command == 'pop_back'):
        deck = pop_back(deck)

    elif(command == 'size'):
        size(deck)

    elif(command == 'empty'):
        empty(deck)

    elif(command == 'front'):
        front(deck)

    else:
        back(deck)
    
    return deck

def main():
    deck = []

    n = singleIntegerInput()

    for i in range(0, n):
        command, data = dataInput()

        deck = judgeCommend(deck, command, data)

# __main__
main()