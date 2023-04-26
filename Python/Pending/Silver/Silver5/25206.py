def main():
    gradeDict = {
        "A+" : 4.5,
        "A0" : 4.0,
        "B+" : 3.5,
        "B0" : 3.0,
        "C+" : 2.5,
        "C0" : 2.0,
        "D+" : 1.5,
        "D0" : 1.0,
        "F" : 0.0
    }
    sumOfScore = 0
    dataResult = 0

    for _ in range(20):
        name, score, grade = input().split()

        if grade == "P":
            pass
        else:
            dataResult += float(score) * gradeDict[grade]
            sumOfScore += float(score)
    
    print(dataResult / sumOfScore)

main()