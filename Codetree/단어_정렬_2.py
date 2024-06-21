al_list = []

n = int(input())
for i in range(n):
    string = input()
    al_list.append([len(string), string])

al_list.sort(key=lambda x:x[1])
al_list.sort(key=lambda x:x[0])

for i in al_list:
    print(i[1])
