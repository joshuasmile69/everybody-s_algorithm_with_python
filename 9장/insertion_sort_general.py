#삽입정렬 알고리즘을 일반화
def insertion_sort_general(a):
    n=len(a)
    for i in range (1,n):
        #i번째 항의 값을 initial로 지정했음
        initial=a[i]
        #i의 바로 앞에 있는 j를 지정
        j=i-1
        #a[j]가 initial보다 크면(즉 해당 값이 initial 뒤에 있어야 하면)
        while j>=0 and a[j]>initial:
            #j+1번째 값을 a[j]로 교체(즉 한칸 뒤로 밀어냄)
            a[j+1]=a[j]
            #그 다음 항(한칸 앞)을 j로 지정
            j-=1
        #이 조건에서 탈출하면 initial이 올 자리를 찾은 것이니 해당 위치에 initial을 삽입
        #(이때 j+1번째 항은 이전 실행에서 a[j]였었을테니, a[j+1]=a[j]라고 하면서 a[j]값이 두개 생겼던 문제는 자연스럽게 해결)
        a[j+1]=initial
    return a

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(insertion_sort_general(a))