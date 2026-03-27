# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
'''모듈러 연산 분배 법칙
a+b=(k1​+k2​)m+(r1​+r2​)
(a+b)modm=((amodm)+(bmodm))modm
'''

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])