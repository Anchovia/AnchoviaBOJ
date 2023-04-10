def main():
    while 1:
        try:
            word = input()
            print(word)

        except EOFError:
            break

main()