# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

#로직 함수
def getMaxValue(stocks, maxWeight):

    dp = [0] * (maxWeight+1)

    #단일 물건의 가치 저장
    for stock in stocks:
        weight, value = stock

        #하향식 메모이제이션 => 역순으로 돌기
        for w in range(maxWeight , weight-1, -1):
            #만약 대응하는 무게가 없다면 자동으로 자기 원래 무게 반영됨
            dp[w] = max(dp[w], dp[w-weight] + value)
            
        
    return dp[maxWeight]

#입력
n, k = list(map(int, input().split()))
stocks = []
for _ in range(n):
    w, v = list(map(int, input().split()))
    stocks.append([w, v])

# n, k = [4, 7]
# stocks = [
#     [6, 13],
#     [4, 8],
#     [3, 6],
#     [5, 12],
# ]

print(getMaxValue(stocks, k))