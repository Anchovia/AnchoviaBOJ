def solution(dataMatrix):
    max = 0
    coordinate = [1, 1]

    for column in range(9):
        for row in range(9):
            if dataMatrix[row][column] > max:
                max = dataMatrix[row][column]
                coordinate = [row + 1, column + 1]
    
    return max, coordinate


def main():
    n = 9
    dataMatrix = [list(map(int, input().split())) for _ in range(n)]
    max, coordinate = solution(dataMatrix)
    print(max)
    print(f"{coordinate[0]} {coordinate[1]}")

main()