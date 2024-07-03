#가짜 동전 찾기 알고리즘
#재귀함수를 도입해서, 범위를 반씩 줄여나가며 대조해보기

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

#이제 재귀함수를 응용해서 만들어보자
def fake_coin_2(left, right):
    #종료조건은 동전이 하나 남을 때, 그 동전이 가짜동전인 순간이 된다
    if left==right:
        return left
    #우선 우리가 재야 하는 범위를 반으로 나눠서
    half=(left+right)//2
    #왼쪽 절반과, 오른쪽 절반을 각각 추에 매달아봅니다
    result=weigh(left, half, half+1, right)
    #왼쪽이 더 가벼우면, 가짜동전은 왼쪽에 있는 거니까 왼쪽에 대해서 다시 작업(재귀)
    if result==-1:
        return fake_coin_2(left,half)
    #오른쪽이 더 가벼우면, 가짜동전은 오른쪽에 있는 거니까 오른쪽에 대해서 다시 작업(재귀)
    elif result==1:
        return fake_coin_2(half+1,right)
    #이도저도 아니라면, left번째부터 right번째까지에는 가짜 동전이 없는 셈입니다
    return "none of them are fake"

n=100
print(fake_coin_2(0,n-1))