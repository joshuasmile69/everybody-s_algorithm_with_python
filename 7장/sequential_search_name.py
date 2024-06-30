#순차탐색 알고리즘-이름과 번호 매칭
#필요한 변수: 학생 번호의 종류(a), 학생 이름(b), 찾고자 하는 값(x)
def sequential_search(a, b, x):
    n=len(a)
    #첫째항부터 마지막 항까지
    for i in range(0, n):
        #i번째 항이 찾고자 하는 값 x와 같은 값이라면
        if a[i]==x:
            #b의 i번째 항(이름)을 return
            return b[i]
    
    #다 찾았는데도 없으면 ?을 return
    return "?"


a=[5, 3, 1, 23, 2, 1, 6, 7, 8, 13, 11, 83, 9]
b=["Anasatasia", "Tom", "Eudokia", "Clementia", "Harold", "Richard", "Blanche", "Alexander", "Raynold", "Anna", "Patricia", "Franz", "Nancy"]
print(sequential_search(a, b, 1))
print(sequential_search(a, b, 13))
print(sequential_search(a, b, 300))