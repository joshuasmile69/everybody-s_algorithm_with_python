#선택정렬 알고리즘을 일반화
#result 리스트 없이 그냥 a 안에서 직접 수정, 최솟값 지정도 따로 함수로 구분 안함
def selection_sort_general(a):
    n=len(a)
    #첫번째부터 n-1번째까지의 항들에 대해서
    for i in range(0, n-1):
        #최솟값을 i번째 항이라고 하고
        min_a=i
        #i+1번째 항부터 n번째 항까지
        for j in range(i+1,n):
            if a[j]<=a[min_a]:
                #최솟값 index를 갱신
                min_a=j
        #i번째 항과 최솟값의 자리를 서로 바꿔줍니다
        a[i], a[min_a] = a[min_a], a[i]
    return a

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(selection_sort_general(a))