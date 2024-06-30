#삽입정렬 알고리즘

#삽입할 값의 삽입할 index 위치를 찾는 함수
def finding_insertion_index(a, b):
    for i in range(0, len(a)):
        #b가 a의 i번째 항보다 작으면
        if b<a[i]:
            #i번째 항에 b를 삽입할 예정이므로 i를 return(이후는 전부 뒤로 한 칸씩 밀림)
            return i
    #아무도 안그러면 b가 최댓값이니까 맨 뒤(len(a))를 return
    return len(a)

def insertion_sort(a):
    #빈 return 리스트를 생성
    result=[]
    #a에 뭔가가 남아있으면
    while a:
        #a의 첫번째 항을 꺼내와서
        insertion=a.pop(0)
        #result 리스트에서 그 뽑은 값이 위치할 index를 찾아서
        insertion_index=finding_insertion_index(result, insertion)
        #해당 index 위치에 뽑아낸 값을 삽입
        result.insert(insertion_index, insertion)
    #다 끝나면 정렬된 result 리스트를 return
    return result

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
print(insertion_sort(a))