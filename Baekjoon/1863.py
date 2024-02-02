'''
'스카이라인 쉬운거'
'''
# 24.02.02 14:39 ~ 15:23 15등했다 뿌듯,,,
import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
answer = 0

for i in range(n):
    x, y = map(int, input().split())
    if stack[-1] < y:               # 이전 고도 보다 현재 고도가 클 경우 건물수 +1
        stack.append(y)
        answer += 1
    elif stack[-1] == y:            # 이전 고도와 같을 경우 continue
        continue
    else:                           # 이전 고도 보다 현재 고도가 작을 경우 이전 고도 pop 한 후 while 문 돌기
        stack.pop()
        while True:
            if stack[-1] > y:       # pop 한 후 마지막 고도가 현재 고도 보다 클 경우 계속 pop
                stack.pop()
            elif stack[-1] == y:    # pop 한 후 마지막 고도가 현재 고도와 같을 경우 while 문 빠져나오기
                break
            else:                   # pop 한 후 마지막 고도가 현재 고도 보다 작을 경우 건물 한 개가 더 있는 것 이므로 건물 수 +1, stack에 넣기
                stack.append(y)
                answer += 1
                break

print(answer)
