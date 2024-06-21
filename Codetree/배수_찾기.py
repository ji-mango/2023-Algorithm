N = int(input())

if N == 1:
    print(3)
elif N == 2:
    print(5)
else:
    index = 1
    while True:
        if 7*index - 4 <= N <= 7*index + 2:
            break
        index += 1

    if N == index * 7 - 4:
        print(3 * (5 * index - 3))
    elif N == index * 7 - 3:
        print(3 * (5 * index - 2))
    elif N == index * 7 - 2:
        print(5 * (3 * index - 1))
    elif N == index * 7 - 1:
        print(3 * (5 * index - 1))
    elif N == index * 7:
        print(5 * (3 * index))
    elif N == index * 7 + 1:
        print(3 * (5 * index + 1))
    elif N == index * 7 + 2:
        print(5 * (3 * index + 1))

