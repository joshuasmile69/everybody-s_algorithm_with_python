#순차탐색 알고리즘-리스트 만들어서 저장하기
def sequential_search(a, x):
#필요한 변수: 리스트 종류(a), 찾고자 하는 값(x)
    result=[]
    #우선 result를 빈 리스트로 지정
    n=len(a)
    for i in range(0, n):
    #첫째항부터 마지막 항까지
        if a[i]==x:
        #i번째 항이 찾고자 하는 값 x와 같은 값이라면
            result.append(i)
            #i를 result 리스트에 추가(set은 add.result지만 얘는 list니까 result.append를 해야함)
        
    return result
    #다 돌리고 나면 result 리스트를 return

a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]

print(sequential_search(a, 1))
print(sequential_search(a, 13))
print(sequential_search(a, 300))