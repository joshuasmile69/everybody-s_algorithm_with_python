#순차탐색 알고리즘
#필요한 변수: 리스트 종류(a), 찾고자 하는 값(x)
def sequential_search(a, x):
    n=len(a)
    #첫째항부터 마지막 항까지
    for i in range(0, n):
        #i번째 항이 찾고자 하는 값 x와 같은 값이라면
        if a[i]==x:
            #i를 return
            return i
 
    #다 찾았는데도 없으면 none을 return        
    return "none"

a=[5, 3, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]

print(sequential_search(a, 1))
print(sequential_search(a, 13))
print(sequential_search(a, 300))