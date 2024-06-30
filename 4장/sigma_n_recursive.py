#재귀함수를 이용한 1부터 n까지의 합 계산
def sigma_n(a):
    #만약 a가 0이면(종료조건)
    if a==0:
        #0을 return
        return 0
        #a가 0보다 크면 a-1까지의 합과 a를 더한 값을 return(재귀)
    return a+sigma_n(a-1)

print(sigma_n(10))