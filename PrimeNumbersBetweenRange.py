def prime(lower, upper):
    l1 = []

    for i in range(lower, upper + 1):
        if i > 1:
            for num in range(2, i):
                if i % num == 0:
                    break
            else:
                l1.append(i)
    return l1

lower = int(input('Enter Lower Limit: '))
upper = int(input('Enter Upper Limit:'))
print(prime(lower, upper))