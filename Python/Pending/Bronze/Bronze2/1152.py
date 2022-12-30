import sys

def main():
    word = 1

    data = sys.stdin.readline().rstrip()

    try:
        if(data[0] == ' '):
            data = data[1:]
        
        if(data[len(data) - 1] == ' '):
            data = data[:len(data) - 1]

        for i in data:
            if(i == ' '):
                word += 1
    
    except IndexError:
        word -= 1
    
    print(word)

# __main__
main()