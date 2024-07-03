#가짜 동전 찾기 알고리즘(혼자 해보는 응용)
#재귀함수를 도입해서, 범위를 1/3로 줄여나가며 대조해보기

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
    #종료조건은 동전이 두개 이하인 것으로 만들어둠(사유: 안그러면 얘는 3등분이라서, left=right에 도달하지 못하고 계속 재귀하다 오류가 남. 따라서 두개 이하로 설정)
    if left==right or left+1==right:
        if weigh(left,left,left+1,left+1)==-1:
            return left
        if weigh(left,left,left+1,left+1)==1:
            return right
        else:
            return "none of them are fake"
    #우선 우리가 재야 하는 범위를 삼등분으로 나눠서
    else:
        dividing_third=(right-left)//3
    #왼쪽 삼등분과, 오른쪽 삼등분을 각각 추에 매달아봅니다
        result=weigh(left, left+dividing_third, right-dividing_third, right)
    #왼쪽이 더 가벼우면, 가짜동전은 왼쪽에 있는 거니까 왼쪽에 대해서 다시 작업(재귀)
        if result==-1:
            return fake_coin_2(left,left+dividing_third)
    #오른쪽이 더 가벼우면, 가짜동전은 오른쪽에 있는 거니까 오른쪽에 대해서 다시 작업(재귀)
        elif result==1:
            return fake_coin_2(right-dividing_third,right)
    #이도저도 아니라면, 일단 왼쪽 삼등분과 오른쪽 삼등분에는 가짜 동전이 없는 셈이니 가운데 삼등분에 대해서 다시 작업(재귀)
        else:
            return fake_coin_2(left+dividing_third,right-dividing_third)

n=100
print(fake_coin_2(0,n-1))