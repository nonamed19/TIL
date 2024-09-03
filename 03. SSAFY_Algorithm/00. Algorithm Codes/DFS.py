def dfs(g, v, visited):
    visited[v] = True  # 현재 노드 v를 방문했음을 표시
    print(v, end=' ')  # 방문한 노드 출력

    for i in g[v]:  # 현재 노드 v와 연결된 모든 노드 i에 대해 반복
        if not visited[i]:  # 노드 i가 아직 방문되지 않았다면
            dfs(g, i, visited)  # 해당 노드 i에 대해 재귀적으로 DFS 수행


g =[[],	[2,3,8], [1,7],	[1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
visited = [False]*9

# adj_l = [[] for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_l[v1].append(v2)    # 무방향인 경우
#     adj_l[v2].append(v1)    # 무방향인 경우

dfs(g,1,visited)