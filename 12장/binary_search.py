#이분탐색 알고리즘
#a는 리스트, x는 찾는 값을 의미함
def binary_search(a,x):
    #찾는 시작지점과, 찾을 범위를 설정
    #시작할 때에는 리스트 전체가 찾을 범위임
    start=0
    end=len(a)-1

    #탐색할 범위가 있는 동안
    while start<=end:
        #범위의 가운데를 잡아서
        mid=(start+end)//2
        #경우 1: mid가 그 찾는 값이면 바로 끝
        if x==a[mid]:
            return mid
        #경우 2: mid가 찾는 값보다 크면 mid의 오른쪽 범위에서 탐색
        if x>a[mid]:
            start=mid+1
        #경우 3: mid가 찾는 값보다 작으면 mid의 왼쪽 범위에서 탐색
        else:
            end=mid-1
    #찾는 값이 없으면 none return
    return "none"

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(a,5))