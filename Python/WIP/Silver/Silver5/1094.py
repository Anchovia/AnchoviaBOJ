import sys

def singleDataInput():
    data = int(sys.stdin.readline().strip())

    return data

def barSumFunc(barList):
    barSumResult = 0

    for i in barList:
        barSumResult += i
    
    return barSumResult
    

def makeToBar(x):
    result = 0
    barList = [64]

    while(True):
        nowBarLength = barSumFunc(barList)

        if(nowBarLength > x):
            pass




    return result

def main():
    x = singleDataInput()