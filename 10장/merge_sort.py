#병합정렬 알고리즘
def merge_sort(a):
    n=len(a)
    #길이가 1보다 작거나 같으면(종료조건)
    if n<=1:
        #a를 return함
        return a
    #mid=n을 절반으로 자른 것(이때 애매하게 소수점 남으면 안되니까 정수 나눗셈 //을 사용)
    mid=n//2
    #그룹 1: 앞쪽 절반([:mid]의 의미: 처음부터 mid까지)에 대해 병합정렬 실행(재귀)
    group1=merge_sort(a[:mid])
    #그룹 2: 뒤쪽 절반([mid:]의 의미: mid부터 끝까지)에 대해 병합정렬 실행(재귀)
    group2=merge_sort(a[mid:])
    #결과를 저장할 빈 리스트
    result=[]
    #경우 1: 그룹 1과 그룹 2가 모두 뭔가 있으면
    while group1 and group2:
        #그룹 1과 그룹 2의 첫항들을 비교해서 그룹 1이 더 작으면
        if group1[0]<group2[0]:
            #그룹 1의 첫항을 꺼내서 result에 넣고
            result.append(group1.pop(0))
        #아니면(그룹 2가 더 작으면)
        else:
            #그룹 2의 첫항을 꺼내서 result에 넣는다
            result.append(group2.pop(0))
    #경우 2: 그룹 1만 뭐가 있으면
    while group1:
        #그룹 1을 차례대로 꺼내서 삽입
        result.append(group1.pop(0))
    #경우 2: 그룹 2만 뭐가 있으면
    while group2:
        #그룹 2를 차례대로 꺼내서 삽입
        result.append(group2.pop(0))

    #result를 return
    return result

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(merge_sort(a))