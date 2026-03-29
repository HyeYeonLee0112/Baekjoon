# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

def getMaxMeeting(meetings):

    #1. 종료시간 순으로, 그 후 같은 종료시간이라면 시작시간 순으로 오름차순 정렬
    meetings.sort(key=lambda meeting:(meeting[1], meeting[0]))

    #2. 가장 빨리 끝나는 회의실부터 선택
    cnt = 1
    endTime = meetings[0][1]
    for meeting in meetings[1:]:
        startTime = meeting[0]
        if(startTime >= endTime):
            endTime = meeting[1]
            cnt += 1
    
    return cnt

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))

print(getMaxMeeting(meetings))