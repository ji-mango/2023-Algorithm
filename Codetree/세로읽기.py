answer = [[] for _ in range(15)]

for i in range(4):
    string = input()
    for j in range(len(string)):
        answer[j].append(string[j])

for i in range(15):
    for j in answer[i]:
        print(j, end='')

