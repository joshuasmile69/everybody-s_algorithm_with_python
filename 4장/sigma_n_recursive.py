#재귀함수를 이용한 1부터 n까지의 합 계산
def sigma_n(a):
    if a==0:
    #만약 a가 0이면(종료조건)
        return 0
        #0을 return
    return a+sigma_n(a-1)
    #a가 0보다 크면 a-1까지의 합과 a를 더한 값을 return(재귀)

print(sigma_n(10))