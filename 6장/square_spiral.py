#사각 나선 알고리즘
import turtle as t
#그림을 그려주는 turtle graphic을 import

def square_spiral(spiral_length):
# 변수: 해당 선의 길이
        if spiral_length<=5:
        #길이가 5 이하이면(종료조건)
            return
            #그냥 return만 해서 종료
        t.forward(spiral_length)
        #그렇지 않다면 우선 적힌 길이만큼 앞으로 전진
        t.right(90)
        #오른쪽으로 90도 회전 (만약 120도면 삼각형이, 60도면 육각형이 나올 것)
        square_spiral(spiral_length-5)
        #길이를 5 감소해서 함수를 다시 호출(재귀)

t.speed(0)
#그림 그리는 속도 조절(이게 제일 빠른듯)
square_spiral(200)
#초기 길이 설정
t.hideturtle()
#거북이 숨기기
t.done()
#그림 다 그렸음을 알려줌