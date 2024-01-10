'''
삼각형과 세 변
'''
# 24.01.10
while True:
    array = list(map(int, input().split()))
    if array[0] == 0 and array[1] == 0 and array[2] == 0:
        break

    array.sort()
    if array[-1] >= array[0] + array[1]:
        print("Invalid")
        continue

    if array[0] == array[1] == array[2]:
        print("Equilateral")
    elif array[0] == array[1] or array[0] == array[2] or array[1] == array[2]:
        print("Isosceles")
    else:
        print("Scalene")

