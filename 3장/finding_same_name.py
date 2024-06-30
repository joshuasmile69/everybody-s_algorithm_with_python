#동명이인 찾기 알고리즘
def finding_same_name(a):
    #n을 리스트의 길이로 지정
    n=len(a)
    #결과는 집합(set)이므로, 순서가 없음
    result=set()
    #첫째 항부터 n-1번째 항까지의 i에 대해
    for i in range (0, n-1):
        #i+1번째 항부터 n번째 항(끝까지)의 j와 비교하여
        for j in range (i+1, n):
            # i번째 항과 j번째 항이 같다면 
            if a[i]==a[j]:
                #result 집합에 i번째 항을 추가
                result.add(a[i])
    #result 집합을 출력(result는 set이므로, list와 다르게 순서가 뒤죽박죽 나와도 상관 없음)
    return result

a=["Anastasia", "Maria", "Caroline", "Maria", "Caroline", "Sophia"]

print(finding_same_name(a))