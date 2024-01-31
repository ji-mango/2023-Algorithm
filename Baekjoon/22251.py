'''
'빌런 호석'
'''
# 24.01.31 15:25 ~ 16:15
# N층까지 이용 가능, K 자리의 수, 최대 P개 반전, 실제 X층
N, K, P, X = map(int, input().split())
LED = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
       [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
       [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
       [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
       [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
       [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
       [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
       [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
       [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
       [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

str_N = str(N)
str_X = str(X)
str_X = '0' * (len(str_N) - len(str_X)) + str_X             # 최대 N개까지만 바꿀 수 있으므로 N개와의 자릿수 차이만큼 X앞에 0 붙이기

answer = 0
for num in range(1, N+1):
    str_num = str(num)
    str_num = '0' * (len(str_X) - len(str_num)) + str_num
    count = 0

    length = len(str_num)
    for i in range(length):
        count += LED[int(str_num[i])][int(str_X[i])]

    if count <= P:
        answer += 1

print(answer-1)     # 자기 자신 빼기
