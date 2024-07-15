def solution(edges):
    counts = {}     # {노드:[나가는 간선의 개수, 들어오는 간선의 개수]}
    for a, b in edges:
        if not counts.get(a):
            counts[a] = [0, 0]
        if not counts.get(b):
            counts[b] = [0, 0]
        counts[a][0] += 1
        counts[b][1] += 1


    answer = [0, 0, 0, 0]   # [생성한 정점의 번호, 도넛 모양 수, 막대 모양 수, 8자 모양 수]
    for node, count in counts.items():
        if count[0] >= 2 and count[1] == 0:     # 생성한 정점 노드
            answer[0] = node
        elif count[0] == 0 and count[1] >= 1:    # 막대 모양 그래프
            answer[2] += 1
        elif count[0] == 2 and count[1] >= 2:   # 8자 모양 그래프
            answer[3] += 1

    answer[1] = counts[answer[0]][0] - answer[2] - answer[3]    # 도넛 모양 그래프

    return answer


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
# print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8],
#                 [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
