while True:
    try:
        data = input()

        blank_index = data.find(' ')

        a = int(data[:blank_index])
        b = int(data[blank_index + 1:])

        print(a + b)
    
    except EOFError:
        break