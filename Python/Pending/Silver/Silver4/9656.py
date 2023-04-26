def solution(rock):
    resultPlayer = ""
    turn = 0

    while rock > 0:
        if rock > 3:
            rock -= 3
            turn += 1
        else:
            rock -= 1
            turn += 1

    if turn % 2 == 0:
        resultPlayer = "SK"
    else:
        resultPlayer = "CY"

    return resultPlayer

def main():
    rock = int(input())

    resultPlayer = solution(rock)

    print(resultPlayer)

main()