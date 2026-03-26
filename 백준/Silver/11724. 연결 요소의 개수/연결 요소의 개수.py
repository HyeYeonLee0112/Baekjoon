# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
import sys
input = sys.stdin.readline

#방문하지 않은 시작 정점을 넣으면 연결된 정점에 대해 visited를 체크함
def dfs_recursion(start, graph, visited):
    for v in graph[start]:
        if(not visited[v]):
            visited[v] = True
            dfs_recursion(v, graph, visited)
            
def dfs_stack(start, graph, visited):

    stack = [start]

    while(stack):

        v = stack.pop()

        for u in graph[v]:
            if(not visited[u]):
                visited[u] = True
                stack.append(u)

#입력 받기
n, m = list(map(int, input().split()))

visited = [False] * (n+1)
# 그래프 초기화
graph = dict()
for key in range(1, n+1):
    graph[key]=[]

# 입력 & 그래프 구성
for _ in range(m):
    u, v = list(map(int, input().split()))

    graph[u].append(v)
    graph[v].append(u)

cnt = 0 #연결 요소의 개수
#연결 요소 세기
for vertex in  range(1, n+1):
    if(not visited[vertex]):
        visited[vertex] = True
        dfs_stack(vertex, graph, visited)
        cnt += 1

print(cnt)
