'''
'틱택토'
'''
# 24.02.02 15:33 ~ 16:37
import sys
input = sys.stdin.readline

def check():            # 누가 이겼는지, X,O 개수 체크
    X_win, O_win = 0, 0
    X_count, O_count = 0, 0
    if game[0] == game[1] == game[2] or game[0] == game[3] == game[6] or game[0] == game[4] == game[8]:
       if game[0] == "X":
           X_win = 1
       elif game[0] == "O":
           O_win = 1
    if game[3] == game[4] == game[5] or game[1] == game[4] == game[7] or game[2] == game[4] == game[6]:
        if game[4] == "X":
            X_win = 1
        elif game[4] == "O":
            O_win = 1
    if game[6] == game[7] == game[8] or game[2] == game[5] == game[8]:
        if game[8] == "X":
            X_win = 1
        elif game[8] == "O":
            O_win = 1

    for i in range(9):
        if game[i] == 'X':
            X_count += 1
        elif game[i] == 'O':
            O_count += 1

    return X_win, O_win, X_count, O_count


while True:
    game = input().strip()
    if game == 'end':
        break

    X_win, O_win, X_count, O_count = check()
    if X_win == 1 and O_win == 1:
        print("invalid")
        continue
    elif X_win == 1 and not(X_count == O_count + 1):
        print("invalid")
        continue
    elif O_win == 1 and not(X_count == O_count):
        print("invalid")
        continue
    elif X_win == 0 and O_win == 0 and (X_count != 5 or O_count != 4):
        print("invalid")
        continue
    else:
        print("valid")
        continue

