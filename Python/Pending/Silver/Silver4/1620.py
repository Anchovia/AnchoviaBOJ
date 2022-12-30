import sys

def singleStrInput():
    s = sys.stdin.readline().rstrip()

    return s

def doubleIntInput():
    a, b = map(int, sys.stdin.readline().rstrip().split())

    return a, b

def printList(l):
    for i in l:
        sys.stdout.write(i)
        sys.stdout.write("\n")

def main():
    pokemonList = []
    resultList = []

    pokemonList_app = pokemonList.append
    resultList_app = resultList.append

    amount, problem = doubleIntInput()

    for i in range(0, amount):
        pokemonName = singleStrInput()
        pokemonList_app(pokemonName)
    
    for j in range(0, problem):
        data = singleStrInput()

        if(data.isdigit()):
            resultList_app(pokemonList[int(data) - 1])

        else:
            resultList_app(str(pokemonList.index(data) + 1))
    
    printList(resultList)

# __main__
main()