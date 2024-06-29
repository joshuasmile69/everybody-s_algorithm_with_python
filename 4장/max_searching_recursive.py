#재귀함수를 이용한 최댓값 찾기
def max_searching(a, n):
#재귀함수를 쓰려면 쓸 때마다 숫자가 하나씩 줄어야 하니까(안그럼 못씀) 길이를 지정해줄 n이라는 변수가 하나 추가로 들어감
    if n==1:
    #만일 길이가 1이면(종료조건)
        return a[0]
        #첫번째 값을 return
    if max_searching(a, n-1)<a[n-1]:
    #길이가 1보다 길면, 마지막 항과 n-1개 길이의 최댓값을 비교해서
        return a[n-1]
        #마지막 항이 더 크면 그 값을 출력
    else:
        return max_searching(a, n-1)
        #아니라면 마지막 항을 제외한 n-1개의 길이의 list에 대해 다시 함수를 실행(재귀)

a=[4, 5, 6, 8, 4, 2, 3, 4, 5, 6, 7, 9]

print(max_searching(a,len(a)))