from collections import defaultdict

N, K = map(int, input().split())

# [{점수:해당 점수 학생의 수}, ...]
score = [defaultdict(int) for _ in range(4)]
for i in range(4):
    input_score = list(map(int, input().split()))
    for j in input_score:
        score[i][j] += 1
    score[i] = sorted(score[i].items())

answer = 0
present = K
for i in score[0]:
    present -= i[0]
    if present < 3:
        present += i[0]
        break
    for j in score[1]:
        present -= j[0]
        if present < 2:
            present += j[0]
            break
        for k in score[2]:
            present -= k[0]
            if present < 1:
                present += k[0]
                break
            for l in score[3]:
                present -= l[0]
                if present < 0:
                    present += l[0]
                    break
                if present == 0:
                    present += l[0]
                    answer += i[1] * j[1] * k[1] * l[1]
                    break
                present += l[0]
            present += k[0]
        present += j[0]
    present += i[0]

print(answer)


