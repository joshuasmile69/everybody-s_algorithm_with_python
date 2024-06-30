#병합정렬 알고리즘을 일반화
def merge_sort_general(a):
    n=len(a)
    #길이가 1보다 작거나 같으면(종료조건)
    if n<=1:
        #그냥 return(종료)
        return
    mid=n//2
    group1=a[:mid]
    group2=a[mid:]
    #반으로 잘라서 merge_sort_general 실행(재귀)
    merge_sort_general(group1)
    merge_sort_general(group2)
    #다 첫항부터 시작할것이므로 카운팅은 0부터 시작
    index_1=0
    index_2=0
    index_a=0
    #경우 1: index 값이 length보다 둘다 작으면(즉 아직 둘 다 끝까지 안갔으면)
    while index_1<len(group1) and index_2<len(group2):
        #두 index 위치에 있는 값들의 크기를 비교해서 그룹 1이 더 작으면
        if group1[index_1]<group2[index_2]:
            #a의 index_a번째 항을 그룹 1의 index_1번째 항으로 교체
            #이때, 그룹 1과 2는 이미 정의되어 있는 애들이라서 a의 항을 교체한다고 그룹 1과 2의 항이 영향을 받지는 않음
            a[index_a]=group1[index_1]
            #써먹은 친구들은 다음 index를 확인하게 넘어감
            index_1+=1
            index_a+=1
        #그룹 2가 더 작으면
        else:
            #위에서 한 일을 그룹 2에 대해 실행
            a[index_a]=group2[index_2]
            index_2+=1
            index_a+=1
    #경우 2: 그룹 1만 남고 그룹 2는 안남았으면
    while index_1<len(group1):
        #그룹 1에 대해 실행
        a[index_a]=group1[index_1]
        index_1+=1
        index_a+=1
    #경우 3: 그룹 2만 남고 그룹 1은 안남았으면
    while index_2<len(group2):
        #그룹 2에 대해 실행
        a[index_a]=group2[index_2]
        index_2+=1
        index_a+=1
    return a

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(merge_sort_general(a))