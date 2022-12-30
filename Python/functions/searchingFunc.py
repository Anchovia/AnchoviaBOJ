def binary_search(target, dataList):
    start = 0
    end = len(dataList) - 1

    while(start <= end):
        mid = (start + end) // 2

        if(dataList[mid] == target):
            return True
        
        elif(dataList[mid] < target):
            start = mid + 1
        
        else:
            end = mid - 1

    return False