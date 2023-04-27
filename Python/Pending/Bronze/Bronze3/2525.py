def main():
    hour, minute = map(int, input().split())
    needTime = int(input())

    minute += needTime

    if minute // 60 > 0:
        cookedHour = minute // 60
        cookedMinute = minute - cookedHour * 60
    else:
        cookedHour = 0
        cookedMinute = minute

    resultHour = hour + cookedHour
    
    if resultHour >= 24:
        resultHour = resultHour - 24
    
    print(f"{resultHour} {cookedMinute}")

main()