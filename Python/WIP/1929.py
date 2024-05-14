def calculatedivisor(data):
    count = 0

    state = True

    maxi = data
    mini = 1
    mid = data // 2

    if data == 1:
        return False
    
    while count < 3 and maxi > mid and mini < mid:
        if state:
            if data % maxi == 0:
                count += 1
            
            maxi -= 1

        else:
            if data % mini == 0:
                count += 1
            
            mini += 1

        state = not state

    if count > 2:
        return False
    else:
        return True

def main():
    strs = ""

    m, n = map(int, input().split())

    for num in range(m, n + 1):
        if(calculatedivisor(num) == True):
            strs += str(num) + "\n"
        
    print(strs, end="")

# __main__
main()