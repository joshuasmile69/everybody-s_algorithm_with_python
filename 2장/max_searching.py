#최댓값 찾기 알고리즘
def max_searching(a):
    #n을 리스트 a의 길이로 설정
    n=len(a)
    #첫번째 항을 a의 최댓값으로 가정
    max_a=a[0]
    #1(즉 리스트의 2번째부터) n-1(즉 리스트의 n째 항(마지막항))까지 범위의 i에 대하여
    for i in range(1, n):
        #만일 가정한 최댓값보다 리스트 a의 i번째 항이 더 큰 값이라면
        if max_a<=a[i]:
            #최댓값을 a의 i번째 항으로 교체
            max_a=a[i]
    #max_a를 return
    return max_a
    

a=[3, 6, 9, 4, 6, 7, 8, 9, 2, 3, 11]
print(max_searching(a))