def main():
    earth, sun, moon = map(int, input().split())

    i, j, k = 1, 1, 1

    count = 1

    while i != earth or j != sun or k != moon:
        i += 1
        j += 1
        k += 1

        if i > 15:
            i = 1

        if j > 28:
            j = 1
        
        if k > 19:
            k = 1
            
        count += 1
    
    print(count)

main()