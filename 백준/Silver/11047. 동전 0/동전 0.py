# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    if(k == 0):
        break

    quotient = k // coin
    if(quotient > 0):
        cnt += quotient
        k -= quotient * coin

print(cnt)