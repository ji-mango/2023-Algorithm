'''
'A와 B 2'
'''
# 24.01.19
S = input()
T = input()

answer = 0


def dfs(A, B):
    global answer
    if answer == 1:
        return

    if len(A) == len(B):
        if A == B:
            answer = 1
            return
    else:
        if A + 'A' in B or (A+'A')[::-1] in B:
            dfs(A + 'A', B)
        if ((A + 'B')[::-1]) in B or (A + 'B') in B:
            dfs((A + 'B')[::-1], B)


dfs(S, T)
print(answer)
