graph = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]

visited = [False]*4


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in range(4):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)

from collections import deque

def bfs(start):
    visited = [False]*4
    q = deque([start])
    visited[start] = True

   



 while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(4):
            if graph[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True

dfs(0)
print()
bfs(0)
