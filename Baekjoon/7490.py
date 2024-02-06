'''
'0 만들기'
'''
# 24.02.06 14:47 ~ 15:20
T = int(input())

cal = [" ", "+", "-"]
def dfs(num, depth, string):
    if depth == num:
        if eval(string.replace(" ", "")) == 0:
            print(string)
    else:
        for i in range(3):
            dfs(num, depth + 1, string + cal[i] + str(depth+1))


for _ in range(T):
    number = int(input())

    dfs(number, 1, "1")
    print()

