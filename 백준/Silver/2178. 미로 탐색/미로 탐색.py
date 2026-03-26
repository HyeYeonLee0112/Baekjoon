# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
import sys
from collections import deque
input = sys.stdin.readline


def four_dir(x, y):
    return [
        [x+1, y], 
        [x-1, y],
        [x, y+1], 
        [x, y-1], 
    ]

def bfs(matrix, row, col):
    
    
    visited = [[False] * col for _ in range(row)]

    cnt = 0
    queue = deque([[0,0, cnt]])

    while(queue):
        #(x, y)좌표로 이동
        x, y, cnt = list(queue.popleft())
        cnt += 1
        
        #도착 여부 확인
        if(x == row-1 and y == col-1):
            return cnt

        #상하좌우 가능성 확인
        for deltaX, deltaY in four_dir(x,y):

            #범위 밖이면 넘기기
            if(deltaX < 0 or deltaY < 0 or
                deltaX > row-1 or deltaY > col-1):
                continue

            if(matrix[deltaX][deltaY] == 1 and not visited[deltaX][deltaY]):
                queue.append([deltaX, deltaY, cnt])
                visited[deltaX][deltaY] = True

    return cnt

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip())))

print(bfs(matrix, n, m))