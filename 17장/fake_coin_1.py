#가짜 동전 찾기 알고리즘
#가장 단순무식한 방법인, 일일이 하나씩 대조해보기

#우선 무게 재는 함수를 지정
#a에서 b까지의 동전과, c에서 d까지의 동전을 비교함
def weigh(a,b,c,d):
    #가짜동전이 37번째 동전이라고 가정, 가짜 동전은 더 가벼움
    fake=37
    #만일 a에서 b사이에 fake 동전이 존재하면, 왼쪽이 더 가벼운 것임(-1로 표기)
    if a<=fake and b>=fake:
        return -1
    #만일 a에서 b사이에 fake 동전이 존재하면, 오른쪽이 더 가벼운 것임(1로 표기)
    if c<=fake and d>=fake:
        return +1
    #둘 다 아니면, 해당 범위 사이에서는 동전이 없는 것
    return 0

#이제, 동전을 일일이 매달아서 확인해보도록 하자
def fake_coin_1(left, right):
    #left+1번째부터 right번째까지의 범위에 대해서
    for i in range(left+1, right+1):
        #left번째와 i번째의 무게를 비교해봅니다
        result=weigh(left, left, i, i)
        #만일 왼쪽이 더 가볍다면 left번째가 가짜동전인 것
        if result==-1:
            return left
        #만일 오른쪽이 더 가볍다면 그 i번째 동전이 가짜동전인 것
        elif result==1:
            return i
    #이도저도 아니라면, left번째부터 right번째까지에는 가짜 동전이 없는 셈입니다
    return "none of them are fake"

n=100
print(fake_coin_1(0,n-1))