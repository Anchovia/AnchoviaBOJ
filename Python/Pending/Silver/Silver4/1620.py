import sys

def searchIntData(pokemonList, data):
    frontIdx = 0
    lastIdx = len(pokemonList) - 1
    midIdx = (lastIdx - frontIdx) // 2 + frontIdx

    while(data != pokemonList[midIdx]):
        if(data < pokemonList[midIdx]):
            lastIdx = midIdx - 1
        
        elif(data > pokemonList[midIdx]):
            frontIdx = midIdx + 1

        midIdx = (lastIdx - frontIdx) // 2 + frontIdx

    return midIdx + 1

def main():
    pokemonList = []

    amount, problem = map(int, sys.stdin.readline().rstrip().split())

    for i in range(0, amount):
        pokemonName = sys.stdin.readline().rstrip()
        pokemonList.append(pokemonName)
    
    for j in range(0, problem):
        data = sys.stdin.readline().rstrip()

        if(data.isdigit()):
            print(pokemonList[int(data) - 1])

        else:
            print(searchIntData(pokemonList, data))

# __main__
main()