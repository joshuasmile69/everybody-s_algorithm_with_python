#두명씩 짝지어주기 알고리즘
def matching_name(a):
    n=len(a)
    #n을 리스트의 길이로 지정
    for i in range (0, n-1):
    #첫째 항부터 n-1번째 항까지의 i에 대해
        for j in range (i+1, n):
        #i+1번째 항부터 n번째 항(끝까지)의 j와 비교하여 
                print(a[i], "-", a[j])
                #i-j 짝지어주기를 출력

a=["Anastasia", "Maria", "Caroline", "Maria", "Caroline", "Sophia"]

matching_name(a)