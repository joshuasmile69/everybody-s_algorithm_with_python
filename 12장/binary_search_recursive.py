#이분탐색 알고리즘을 재귀함수로 쪼개서 만들어보기

#특정 범위에서 이분탐색을 실행하는 함수. a는 리스트, x는 찾는 값을, start와 end는 탐색 범위를 의미함
def binary_search_sub(a,x, start, end):
    #찾을 범위 전체에 없으면(종료조건) none을 return
    if start>end:
        return "none"

    mid=(start+end)//2
    #경우 1: mid가 그 찾는 값이면 바로 끝
    if x==a[mid]:
        return mid
    #경우 2: mid가 찾는 값보다 크면 mid의 오른쪽 범위에서 탐색
    elif x>a[mid]:
        return binary_search_sub(a,x, mid+1, end)
    #경우 3: mid가 찾는 값보다 작으면 mid의 왼쪽 범위에서 탐색
    else:
        return binary_search_sub(a,x, start, mid-1)

#리스트 전체에 대하여 탐색을 실행
def binary_search(a,x):
        return binary_search_sub(a, x, 0, len(a)-1)

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(a,5))