import sys

def solution(number):
    strList = str(number) + ' ='
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
            strList += f' {i} +'
    if number == sum:
        return strList[:(len(strList) - 2)]
    else:
        return f"{number} is NOT perfect."
            

def main():
    while True:
        number = int(sys.stdin.readline())
        if number == -1:
            break
        else:
            strs = solution(number)
            print(strs)

main()