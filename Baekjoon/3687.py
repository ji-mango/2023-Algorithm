'''
'성냥개비'
'''

# 24.03.29 23:20 ~
T = int(input())
INF = int(1e20)

d = [[str(INF)] for i in range(101)]
d[2], d[3], d[4], d[5], d[6], d[7] = ['1'], ['7'], ['4'], ['2'], ['6'], ['8']
for i in range(8, 101):
    for j in range(2, 2 + i // 2):
        temp = d[j] + d[i - j]
        temp.sort()
        index = -1

        for k in range(1, len(temp)):
            if temp[k] == '6' or temp[k] == '9':
                temp[k] = '0'

        for k in range(len(temp)):
            if temp[k] != '0':
                index = k
                break

        temp[0], temp[index] = temp[index], temp[0]
        if temp[0] == '0':
            temp[0] = '6'

        tempToString = ''
        for k in temp:
            tempToString += k

        dToString = ''
        for k in d[i]:
            dToString += k
        if int(dToString) > int(tempToString):
            d[i] = temp

for i in range(T):
    n = int(input())

    maxNum = ''
    if n % 2 == 0:
        maxNum = '1' * (n // 2)
    else:
        maxNum = '7' + '1' * (n // 2 - 1)

    minNum = ''
    for s in d[n]:
        minNum += s

    print(int(minNum), int(maxNum))


# 예외 1, 83 (688888888888)