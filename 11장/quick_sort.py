#퀵정렬 알고리즘
def quick_sort(a):
    n=len(a)
    #길이가 1보다 작거나 같으면(종료조건)
    if len(a)<=1:
        return a
    #pivot은 기준점 역할을 할 예정(지금은 제일 마지막 값을 기준으로 삼았음)
    pivot=a[-1]
    group1=[]
    group2=[]
    #pivot으로 지정된 마지막 값을 제외한 나머지 항들에 대해서
    for i in range(0, n-1):
        #기준값보다 작으면
        if a[i]<pivot:
            #그룹 1로 보내기
            group1.append(a[i])
        #기준값보다 크면
        else:
            #그룹 2로 보내기
            group2.append(a[i])
    
    #재귀함수 사용, 그룹 1의 정렬+기준점+그룹 2의 정렬값으로 만든 리스트를 return
    return quick_sort(group1)+[pivot]+quick_sort(group2)

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(quick_sort(a))