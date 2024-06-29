#최솟값 찾기 알고리즘
def min_searching(a):
    n=len(a)
    #n을 리스트 a의 길이로 설정
    min_a=a[0]
    #첫번째 항을 a의 최솟값이라고 가정
    for i in range(1,n):
    #2번째부터 n번째까지의 i에 대하여
        if a[i]<min_a:
        #a의 i번째 항이 가정한 a의 최솟값보다 작다면
            min_a=a[i]
            #a의 최솟값을 그 i번째 항으로 교체
    return(min_a)
    #min_a 값을 return

a=[3, 6, 9, 4, 6, 7, 8, 9, 2, 3, 11]
print(min_searching(a))