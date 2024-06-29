#최댓값의 index(항 순서) 찾기 알고리즘
def max_searching_index(a):
    n=len(a)
    #n을 리스트 a의 길이로 설정
    max_a=0
    #첫번째 항을 a의 최댓값으로 가정(즉 리스트의 0번째 index)
    for i in range(1, n):
    #1(즉 리스트의 2번째부터) n-1(즉 리스트의 n째 항(마지막항))까지 범위의 i에 대하여
        if max_a<=a[i]:
        #만일 가정한 최댓값보다 리스트 a의 i번째 항이 더 큰 값이라면
            max_a=i
            #최댓값을 a의 i번째 항으로 교체, index도 그에 맞게 변경
    return max_a
    #max_a를 return

a=[3, 6, 9, 4, 6, 7, 8, 9, 2, 3, 11]
print(max_searching_index(a))