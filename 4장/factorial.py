#팩토리얼(!) 계산하기

def factorial_1(a):
#방법 1: 정석적으로 1부터 n까지를 계산하여 팩토리얼 구하기
    s=1
    #초기값:1
    for i in range(1, a+1):
    #1부터 a까지(a+1 포함 안됨)의 i에 대하여
        s=s*i
        #s에 i를 계속 곱함
    return s
    #s를 return

def factorial_2(a):
#방법 2: 재귀함수(recursive!)를 사용
    if a<=1:
    #a가 1 이하(0!도 1이니까)이면(종료조건)
        return 1
        #1을 return
    return a*factorial_2(a-1)
    #그렇지 않다면, a-1번째의 팩토리얼을 계산해서 a랑 곱한 값을 return(재귀)

print(factorial_1(5))
print(factorial_2(5))