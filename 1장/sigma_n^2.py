#제곱수 더하기 알고리즘
import math

def sigma_n_1(a):
#방법 1: 수학적 공식 이용(1~n의 제곱의 합=n(n+1)(2n+1)/6)
    return a*(a+1)*(2*a+1)//6

def sigma_n_2(a):
#방법 2: 일일이 노가다 뛰기(1부터 n까지 각 항의 제곱을 다 더함)
    s=0
    #s를 변수로 설정
    for i in range(1, a+1):
    #i:1부터 n까지 (range(1,n+1)은 1부터 n까지만을 생성, n+1은 포함 안함)
        s=s+i*i
    #i*i를 s값에 지속적으로 추가
    return s
    #s를 return

print(sigma_n_1(10))
print(sigma_n_2(10))