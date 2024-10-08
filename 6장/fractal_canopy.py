#프랙탈 나무 알고리즘
import turtle as t

#변수: 가지의 길이(branch_length)
def fractal_canopy(branch_length):
    #가지 길이가 5보다 작으면(종료조건)
    if branch_length<=5:
        #추가 내용 없이 return
        return
    #새로운 가지의 길이는 원래 가지 길이의 절반으로 지정
    new_length = branch_length*0.5
    #우선 가지 길이만큼 그린 후에
    t.forward(branch_length)
    #오른쪽으로 20도 꺾어서
    t.right(20)
    #새로운 가지 길이를 기준으로 다시 나무를 그리고
    fractal_canopy(new_length)
    #왼쪽으로 40도 꺾어서(그럼 원래 줄기 기준으로는 왼쪽 20도가 됨)
    t.left(40)
    #새로운 가지 길이를 기준으로 다시 나무를 그리고
    fractal_canopy(new_length)
    #다시 20도 꺾어서(원래 방향과 일치시키기)
    t.right(20)
    #돌아오기!
    t.backward(branch_length)

t.speed(0)
#나무는 위로 자라니까 왼쪽 90도 회전
t.left(90)
fractal_canopy(200)
t.hideturtle()
t.done()