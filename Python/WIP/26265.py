import sys

def main():
    dataDict = dict()
    mentoList = list()

    case = int(input())

    for _ in range(case):
        mento, mentee = list(sys.stdin.readline().rstrip().split())

        if mento in dataDict:
            dataDict[mento].append(mentee)
        else:
            dataDict[mento] = [mentee]
            mentoList.append(mento)

    mentoList.sort()

    for key, value in dataDict.items():
        dataDict[key] = sorted(value, reverse=True)

    for nowMento in mentoList:
        nowMenteeList = dataDict[nowMento]

        for nowMenTee in nowMenteeList:
            print(f"{nowMento} {nowMenTee}")

main()