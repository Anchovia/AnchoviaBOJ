import string

def main():
    newWord = ""

    strs = input()

    for word in strs:
        if word.isupper():
            newWord += word.lower()
        
        else:
            newWord += word.upper()

    print(newWord)

main()