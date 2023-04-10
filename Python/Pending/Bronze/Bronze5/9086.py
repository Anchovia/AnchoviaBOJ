def main():
    testCase = int(input())
    
    for _ in range(testCase):
        word = input()

        print(word[0] + word[len(word) - 1])

main()