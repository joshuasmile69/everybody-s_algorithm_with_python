#피보나치 수열 알고리즘
def fibonacci(a):
    if a<=1:
    #피보나치 수열의 첫째, 둘째값은 1이므로(종료조건)
        return a
    #a를 return
    return fibonacci(a-1)+fibonacci(a-2)
    # a번째 피보나치 수열은 a-1번째와 a-2번째를 더하여 return(재귀)

print(fibonacci(10))