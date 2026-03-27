# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
import sys
line = sys.stdin.readline().split('-')

result = 0
for index, element in enumerate(line):
    
    sum = 0
    for add in element.split('+'):
        sum += int(add)

    if(index == 0):
        result += sum
    else:
        result -= sum
print(result)