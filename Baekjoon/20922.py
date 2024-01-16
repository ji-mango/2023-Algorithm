'''
'겹치는 건 싫어'
'''
# 24.01.16
from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))
dic = defaultdict(int)

length = 0
max_len = 0
cursor = 0
for i in range(N):
    if dic[array[i]] + 1 > K:
        max_len = max(length, max_len)
        for k in range(cursor, i):
            if array[k] == array[i]:
                cursor = k+1
                break
            else:
                 dic[array[k]] -= 1
                 length -= 1
    else:
        dic[array[i]] += 1
        length += 1

print(max(max_len, length))


