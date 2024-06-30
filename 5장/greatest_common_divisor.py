#최대공약수 계산 알고리즘
#방법 1: 둘 중 더 작은 애를 기준으로, 숫자값을 하나씩 내려보면서 확인함
def greatest_common_divisor_1(a,b):
    #i: 둘 중 더 작은 애
    i=min(a,b)
    #계속 작동시키기 시작
    while True:
        #i가 a와 b를 모두 나눌 수 있다면(최대공약수라면)
        if a%i==0 and b%i==0:
            #i를 return
            return i
        #아니었다면 i값을 하나 줄여서 다시 해보기
        i=i-1

#방법 2: 유클리드 호제법을 이용한 재귀함수 호출
#유클리드 호제법이란? a와 b의 최대공약수 = 둘 중 더 작은 값과 (b라고 가정) 큰값을 b로 나눈 나머지(a%b)의 최대공약수
def greatest_common_divisor_2(a,b):
    #만약 b가 0이라면(b가 0이라는 건 호제법 상 나머지가 없다는 뜻이며, 곧 최대공약수를 찾았다는 뜻. 그게 아니더라도 b=0일 경우 그냥 0과 어떤 수의 최대공약수는 어떤 수 자체이다)(종료조건)
    if b==0:
        #a를 return(이전의 b에 대해 b%a가 0인거니까, 결과적으로 a가 최대공약수)
        return a
    #아직 안나눠졌다면, b와 a를 b로 나눈 나머지를 return(유클리드 호제법 사용, a가 b보다 작더라도 이 과정을 한 번 거치면 그 다음에는 b가 a를 나누게 되므로 a,b의 크기 구분 필요 없음)
    return greatest_common_divisor_2(b, a%b)
    
print(greatest_common_divisor_1(21, 27))
print(greatest_common_divisor_2(21, 27))