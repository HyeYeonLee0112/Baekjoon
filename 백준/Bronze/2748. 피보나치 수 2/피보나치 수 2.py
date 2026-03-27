# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys

def fibonacci(n, memo):
    if(n == 0 or n==1):
        memo[n] = n
        return n
    
    #오직 최적화를 위해?
    if(memo[n] != -1):
        return memo[n]

    #메모에 없으면 메모이제이션
    else:
        memo[n] = fibonacci(n-2, memo) + fibonacci(n-1, memo)

    return memo[n]


n = int(sys.stdin.readline())
memo = [-1] * (n+1)
print(fibonacci(n, memo))