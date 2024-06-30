#버블정렬 알고리즘
def bubble_sort(a):
    n=len(a)
    #정렬이 끝날 때까지, 계속 반복
    while True:
        #우선 시작할 때에는 changed가 False 상태로 시작
        changed=False
        #자료를 앞에서부터 쭉 따라오면서, 자리바꿔줄 애들은 자리를 바꿔주고 바꿔줬다고 표시
        for i in range(0,n-1):
            #i번째 항이 i+1번째 항보다 크면
            if a[i]>a[i+1]:
                #두 자료의 위치를 서로 맞교환해주고
                a[i], a[i+1] = a[i+1], a[i]
                #자료가 변했으니 changed에 True 입력
                changed=True
        #이 행위를 다 끝냈는데 changed가 False면 바뀐것 없음, 즉 정렬이 완료됨
        if changed==False:
            return a
        
a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(bubble_sort(a))