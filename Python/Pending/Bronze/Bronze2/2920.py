import sys

def main():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    ac = 0
    dc = 0
    
    for i in range(0, 8):
        if(dataList[i] == i + 1 and ac >= dc):
            ac += 1
        
        elif(dataList[i] == 8 - i and dc >= ac):
            dc += 1
        
        else:
            pass
    
    if(ac == 8):
        print("ascending")
    
    elif(dc == 8):
        print("descending")
    
    else:
        print("mixed")

# __main__
main()