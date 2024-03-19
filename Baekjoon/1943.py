'''
'동전 분배'
'''

# 24.03.19 17:07 ~
import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    total = 0
    coins = []
    for i in range(N):
        a, b = map(int, input().split())
        total += a * b
        coins.append([a, b])

    if total % 2 == 0:
        goal = total // 2
        dp = [True] + [False] * goal

        answer = 0
        for i in range(len(coins)):
            coin, num = coins[i]

            for j in range(goal, coin-1, -1):
                if dp[j-coin]:
                    for k in range(num):
                        if j + coin * k <= goal:
                            dp[j + coin * k] = True
                        else:
                            break

            if dp[-1]:
                answer = 1
        print(answer)

    else:
        print(0)


