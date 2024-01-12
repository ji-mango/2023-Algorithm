'''
'스위치 켜고 끄기'
'''
# 24.01.12
import math

def change(middle):
    switch[middle] = 0 if switch[middle] else 1
    count = 0
    while True:
        left = middle - (count+1)
        right = middle + (count+1)
        if left < 0 or right >= N:
            break
        elif switch[left] == switch[right]:
            count += 1
            if switch[left]:
                switch[left] = 0
                switch[right] = 0
            else:
                switch[left] = 1
                switch[right] = 1
        else:
            break

    return count


N = int(input())
switch = list(map(int, input().split()))

S = int(input())
for i in range(S):
    gender, number = map(int, input().split())

    if gender == 1:     # 남자면
        temp = 1
        new_num = number
        while True:
            new_num = number * temp
            if new_num > N:
                break
            switch[new_num-1] = 0 if switch[new_num-1] else 1
            temp += 1


    elif gender == 2:
        change(number-1)

result = math.ceil(N // 20)
for i in range(result+1):
    if i == result:
        print(*switch[20 * i:])
    else:
        print(*switch[20 * i:20*(i+1)])
