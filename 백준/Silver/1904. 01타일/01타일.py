# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
'''모듈러 연산 분배 법칙
a+b=(k1​+k2​)m+(r1​+r2​)
(a+b)modm=((amodm)+(bmodm))modm
'''
import sys

def getTileNums(n, memo):
    if(memo.get(n) != None):
        return memo[n]

    for index in range(1, n+1):
        if(index == 1 or index == 2):
            memo[index] = index
            continue

        memo[index] = (memo[index-1] + memo[index-2]) % 15746 
    
    return memo[n]

n = int(sys.stdin.readline())
memo = dict()
print(getTileNums(n, memo))