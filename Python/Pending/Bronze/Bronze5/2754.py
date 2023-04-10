def main():
    grade = input()

    if grade == "A+":
        score = 4.3
    elif grade == "A0":
        score = 4.0
    elif grade == "A-":
        score = 3.7
    elif grade == "B+":
        score = 3.3
    elif grade == "B0":
        score = 3.0
    elif grade == "B-":
        score = 2.7
    elif grade == "C+":
        score = 2.3
    elif grade == "C0":
        score = 2.0
    elif grade == "C-":
        score = 1.7
    elif grade == "D+":
        score = 1.3
    elif grade == "D0":
        score = 1.0
    elif grade == "D-":
        score = 0.7
    else:
        score = 0.0

    print(score)

main()