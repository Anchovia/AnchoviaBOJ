def main():
    pass

def test():
    for n in range(1, 15):
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    count += 1
        print(count)
test()
main()