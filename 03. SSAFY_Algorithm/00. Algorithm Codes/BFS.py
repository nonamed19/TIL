from collections import deque

def bfs(g, v, visited):
    queue = deque([v])  # 시작 노드를 큐에 추가
    visited[v] = True  # 시작 노드를 방문했음을 표시

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐의 가장 앞에 있는 노드를 꺼냄
        print(v, end=' ')  # 방문한 노드 출력

        for i in g[v]:  # 현재 노드 v와 연결된 모든 노드 i에 대해 반복
            if not visited[i]:  # 노드 i가 아직 방문되지 않았다면
                queue.append(i)  # 노드 i를 큐에 추가
                visited[i] = True  # 노드 i를 방문했음을 표시


g =[[],	[2,3,8], [1,7],	[1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
visited = [False]*9

# adj_l = [[] for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_l[v1].append(v2)    # 무방향인 경우
#     adj_l[v2].append(v1)    # 무방향인 경우

bfs(g,1,visited)