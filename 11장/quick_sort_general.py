#퀵정렬을 일반화함

#특정 범위에 대해 퀵정렬을 시킬 함수
def quick_sort_general_sub(a, start, end):
    #항이 하나 이하이면(종료조건)
    if end-start<=0:
        return
    #기준점: 마지막 값으로 설정
    pivot=a[end]
    #i는 첫항부터 시작
    i=start
    for j in range(start, end):
        #pivot보다 작은 값이면
        if a[j]<=pivot:
            #pivot과 위치를 바꿈
            a[i], a[j] = a[j], a[i]
            #i를 하나씩 늘려가면서 실행
            i+=1
    #마지막으로 end에 있는 애와 i번째 항을 교체
    #이게 없으면 end를 기준점으로 설정했는데 기준점이 여전히 맨 끝에 있게 됨(기준점은 i, 즉 pivot보다 작은 애 뒤, pivot보다 큰 애 앞에 있는 지점으로 이동해야 함)
    a[i], a[end] = a[end], a[i]
    # 기준점보다 작은 그룹(a, start, i-1)과 기준점보다 큰 그룹(a, i+1, end)에 대해 반복(기준점(pivot)은 이미 원하는 위치에 놓인거니까 굳이 안함)
    quick_sort_general_sub(a, start, i-1)
    quick_sort_general_sub(a, i+1, end)

#리스트 전체를 범위로, 퀵정렬시킴
def quick_sort_general(a):
    quick_sort_general_sub(a, 0, len(a)-1)
    return a

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(quick_sort_general(a))