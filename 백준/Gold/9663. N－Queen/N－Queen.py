# 백트래킹 - N-Queen (백준 골드4)

# 문제 링크: https://w

# ` bvcww.acmicpc.net/problem/9663


import sys


col = 0
right = 0
left = 0

def visit(n, index):
    n ^= (1<<index)
    return n

def isVisited(n, x, y):
    return (
        col   & (1 << x) or
        right & (1 << (x + y)) or
        left  & (1 << (x - y + N))
    )

cnt = 0
def solve(y: int, n: int):
    global col, right, left, cnt
    if y >= n:
        cnt += 1
        return
    for x in range(n):
        if isVisited(n, x, y): continue
        col = visit(col, x)
        right = visit(right, x + y)
        left = visit(left, x + N - y)
        solve(y + 1, n)
        col = visit(col, x)
        right = visit(right, x + y)
        left = visit(left, x + N - y)

    pass


N = int(input())

solve(0, N)

print(cnt)