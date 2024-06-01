import sys

def solution(number):
    strList = str(number) + ' ='
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
            strList += f' {i} +'
    if number == sum:
        return strList
    else:
        return f"{number} is NOT perfect."
            

def main():
    number = int(sys.stdin.readline())
    strs = solution(number)
    print(strs)

main()