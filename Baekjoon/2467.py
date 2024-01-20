'''
'용액'
'''
# 24.01.20
N = int(input())
board = list(map(int, input().split()))

minimum = 2000000001
answer_left = 0
answer_right = 0
left = 0
right = N-1

while True:
    if left >= right:
        break

    combine = board[left] + board[right]
    if abs(combine) < minimum:
        minimum = abs(combine)
        answer_left, answer_right = left, right
        if minimum == 0:
            break

    if combine < 0:
        left += 1
    elif combine > 0:
        right -= 1

print(board[answer_left], board[answer_right])
