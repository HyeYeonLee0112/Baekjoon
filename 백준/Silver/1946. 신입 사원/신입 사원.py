# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

def getNums(rankList):

    #"서류심사 순위"를 기준으로 순위 리스트 오름차순 정렬
    rankList.sort(key=lambda rank: rank[0])

    #서류 성적 좋은 사람의 인터뷰 성적
    max_interview_rank = rankList[0][1]
    cnt = 1 #선발인원(서류 1등 채용)
   
    for employee in rankList[1:]:
        interview_rank = employee[1]

         #현재 m_i_r보다 순위가 높으면 선발
        if(interview_rank < max_interview_rank):
            cnt += 1
            max_interview_rank = interview_rank
    
    return cnt

t = int(input())
tc =  [[] for _ in range(t)]
result = [] #결과

#테스트 케이스 입력
for i in range(t):
    n = int(input())

    #순위 입력
    for _ in range(n):
        rank = list(map(int, input().split()))
        tc[i].append(rank)

    #계산
    r = getNums(tc[i])
    result.append(r)


#결과 출력
for r in result:
    print(r)