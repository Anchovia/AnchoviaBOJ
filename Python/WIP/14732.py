def main():
    result = 0

    testCase = int(input())

    for _ in range(testCase):
        x1, y1, x2, y2 = map(int, input().split())

        result += (x2 - x1) * (y2 - y1)
    
    print(result)

main()