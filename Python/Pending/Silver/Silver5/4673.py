def d(n):
    result = 0

    for i in str(n):
        result += int(i)
    
    result += n

    return result

sets = set([])
set_number = set([])

for i in range(1, 10000):
    set_number.add(i)

    if(d(i) < 10000):
        sets.add(d(i))
    
    else:
        pass

result = set_number - sets
result = list(result)

result.sort()

for i in result:
    print(i)