from sys import stdin

def solution(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return "Invalid"
    elif x < 1 or y < 1 or z < 1:
        return "Invalid"
    elif x >= y + z or y >= x + z or z >= x + y:
        return "Invalid"
    elif x == y == z:
        return "Equilateral"
    elif x == y or y == z or z == x:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    while True:
        x, y, z = map(int, stdin.readline().rstrip().split())
        if x == y == z == 0:
            break
        else:
            strs = solution(x, y, z)
            print(strs)

main()