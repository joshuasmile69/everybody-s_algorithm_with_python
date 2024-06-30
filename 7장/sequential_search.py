#순차탐색 알고리즘
def sequential_search(a, x):
#필요한 변수: 리스트 종류(a), 찾고자 하는 값(x)
    n=len(a)
    for i in range(0, n):
    #첫째항부터 마지막 항까지
        if a[i]==x:
        #i번째 항이 찾고자 하는 값 x와 같은 값이라면
            return i
            #i를 return
        
    return "none"
    #다 찾았는데도 없으면 none을 return

a=[5, 3, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]

print(sequential_search(a, 1))
print(sequential_search(a, 13))
print(sequential_search(a, 300))