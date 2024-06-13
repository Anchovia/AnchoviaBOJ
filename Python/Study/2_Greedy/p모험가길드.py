def solution(memberList):
    result = 0
    count = 0
    memberList.sort()
    for now in memberList:
        count += 1
        if count >= now:
            result += 1
            count = 0

    return result

def main():
    n = int(input())
    memberList = list(map(int, input().split()))
    result = solution(memberList)
    print(result)

main()