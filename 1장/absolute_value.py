#절댓값 구하기 알고리즘
import math
#방법 1: 경우를 나누어 풀어보기
def absolute_value_1(a): 
#a가 0보다 크면 a를 그대로 return
  if a>=0:
    return a
#a가 0보다 작으면 -a를 return
  else:
    return -a

#방법 2: 제곱해서 제곱근을 씌우기
def absolute_value_2(a):
  b=a*a
  print(math.sqrt(b))

print(absolute_value_1(4))
print(absolute_value_2(-7))