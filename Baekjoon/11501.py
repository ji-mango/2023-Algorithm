import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    price = 0
    max_value = stock[-1]
    for i in range(N-2, -1, -1):
        if stock[i] > max_value:
            max_value = stock[i]
        else:
            price += max_value - stock[i]

    print(price)
