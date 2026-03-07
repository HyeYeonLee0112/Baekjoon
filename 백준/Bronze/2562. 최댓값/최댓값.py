# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
import sys #인풋을 더 빠르게 하는 메서드를 지원하는 모듈

#list = sys.stdin.readline()
myList = []

for line in sys.stdin: #입력 개수는 상수가 아님
    myList.append(int(line.strip()))  
    #strip메서드로 줄바꿈 문자 '\n제거' 후 string에서 int형으로

max, maxIndex = 0, 0

for i in range(len(myList)):
    if(myList[i] > max):
        max = myList[i]
        maxIndex = i

print(max, maxIndex+1)