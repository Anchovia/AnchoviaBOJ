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

def add(setList, x):
    if(x in setList):
        pass
    
    else:
        setList.append(x)

    return setList

def remove(setList, x):
    if(x in setList):
        setList.remove(x)
    
    else:
        pass
    
    return setList

def check(setList, x):
    if(x in setList):
        print(1)
    
    else:
        print(0)

def toggle(setList, data):
    if(data in setList):
        setList.remove(data)
    
    else:
        setList.append(data)
    
    return setList

def all():

    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def empty():
    return []

def judgCmd(setList, cmd, data):
    if(cmd == 'add'):
        setList = add(setList, data)
    
    elif(cmd == 'remove'):
        setList = remove(setList, data)
    
    elif(cmd == 'check'):
        check(setList, data)
    
    elif(cmd == 'toggle'):
        setList = toggle(setList, data)
    
    elif(cmd == 'all'):
        setList = all()
    
    elif(cmd == 'empty'):
        setList = empty()

    return setList

def main():
    setList = []

    run = singleIntInput()

    for i in range(0, run):
        cmd, data = dataInput()
        setList = judgCmd(setList, cmd, data)

# __main__
main()