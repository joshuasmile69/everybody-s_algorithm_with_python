#선택정렬 알고리즘

<<<<<<< HEAD
#우선 최솟값을 찾는 알고리즘을 만든다
def min_searching_index(a):
    #n을 리스트 a의 길이로 설정
    n=len(a)
    #첫번째 항을 a의 최솟값으로 가정(즉 리스트의 0번째 index)
    min_a=0
    #1(즉 리스트의 2번째부터) n-1(즉 리스트의 n째 항(마지막항))까지 범위의 i에 대하여
    for i in range(1, n):
        #만일 가정한 최솟값보다 리스트 a의 i번째 항이 더 작은 값이라면
        if a[min_a]>=a[i]:
            #최솟값을 a의 i번째 항으로 교체, index도 그에 맞게 변경
            min_a=i
    #min_a를 return
    return min_a

def selection_sort(a):
    #result를 빈 리스트로 생성
    result=[]
    #리스트 a가 비어있지 않는 동안
    while a:
        #가장 작은 값의 index를 찾아서
        min_a=min_searching_index(a)
        #그 값을 pop으로 꺼내고 next_one으로 지정
        next_one=a.pop(min_a)
        #next_one 값을 result 리스트에 추가
        result.append(next_one)
=======
def min_searching_index(a):
#우선 최솟값을 찾는 알고리즘을 만든다
    n=len(a)
    #n을 리스트 a의 길이로 설정
    min_a=0
    #첫번째 항을 a의 최솟값으로 가정(즉 리스트의 0번째 index)
    for i in range(1, n):
    #1(즉 리스트의 2번째부터) n-1(즉 리스트의 n째 항(마지막항))까지 범위의 i에 대하여
        if a[min_a]>=a[i]:
        #만일 가정한 최솟값보다 리스트 a의 i번째 항이 더 작은 값이라면
            min_a=i
            #최솟값을 a의 i번째 항으로 교체, index도 그에 맞게 변경
    return min_a
    #min_a를 return

def selection_sort(a):
    result=[]
    #result를 빈 리스트로 생성
    while a:
    #리스트 a가 비어있지 않는 동안
        min_a=min_searching_index(a)
        #가장 작은 값의 index를 찾아서
        next_one=a.pop(min_a)
        #그 값을 pop으로 꺼내고 next_one으로 지정
        result.append(next_one)
        #next_one 값을 result 리스트에 추가
>>>>>>> 36d1208e825c7fa79e71da58b130749864dc8d0a
    return result

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(selection_sort(a))