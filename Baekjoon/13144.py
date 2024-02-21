'''
'List of Unique Numbers'
'''
# 24.02.21 14:16 ~ 15:54
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))
answer = N

left = 0
right = 0
dic = defaultdict(int)
dic[array[0]] = 1
while True:
    if left == right:
        right += 1
        if right >= N:
            break
        dic[array[right]] += 1
    elif dic[array[right]] > 1:
        dic[array[left]] -= 1
        left += 1
    else:
        answer += right - left
        right += 1
        if right >= N:
            break
        dic[array[right]] += 1

print(answer)
