#사각 나선 알고리즘
import turtle as t
#그림을 그려주는 turtle graphic을 import

# 변수: 해당 선의 길이
def square_spiral(spiral_length):
        #길이가 5 이하이면(종료조건)
        if spiral_length<=5:
            #그냥 return만 해서 종료
            return
        #그렇지 않다면 우선 적힌 길이만큼 앞으로 전진
        t.forward(spiral_length)
        #오른쪽으로 90도 회전 (만약 120도면 삼각형이, 60도면 육각형이 나올 것)
        t.right(90)
        #길이를 5 감소해서 함수를 다시 호출(재귀)
        square_spiral(spiral_length-5)

#그림 그리는 속도 조절(이게 제일 빠른듯)
t.speed(0)
#초기 길이 설정
square_spiral(200)
#거북이 숨기기
t.hideturtle()
#그림 다 그렸음을 알려줌
t.done()