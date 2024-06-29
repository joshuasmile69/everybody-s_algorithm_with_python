#시에르핀스키 삼각형 알고리즘
import turtle as t
#그림을 그려주는 turtle graphic을 import

def sierpinski_triangle(triangle_length):
# 변수: 해당 선의 길이
        if triangle_length<=10:
        #길이가 10보다 작으면(종료조건)
            for i in range(0, 3):
            #i=0에서 2까지(즉 총 3번)
                t.forward(triangle_length)
                t.left(120)
                #앞으로 가고 120도 회전해서 삼각형을 그림
            return
        new_length = triangle_length / 2
        #원래 삼각형 길이의 절반을 정의
        sierpinski_triangle(new_length)
        #해당 길이를 가지고 다시 시에르핀스키 삼각형을 그림(재귀)
        t.forward(new_length)
        #앞으로 가서 또다른 삼각형 그릴 준비
        sierpinski_triangle(new_length)
        #해당 길이를 가지고 다시 시에르핀스키 삼각형을 그림(재귀)
        t.backward(new_length)
        t.left(60)
        t.forward(new_length)
        t.right(60)
        #아직 안 그린 삼각형 그림 그릴 시작점으로 이동
        sierpinski_triangle(new_length)
        #해당 길이를 가지고 다시 시에르핀스키 삼각형을 그림(재귀)
        t.left(60)
        t.backward(new_length)
        t.right(60)
        # 다음 차의 시에르핀스키 그림을 그리게 이동

t.speed(0)
#그림 그리는 속도 조절(이게 제일 빠른듯)
sierpinski_triangle(200)
#초기 길이 설정
t.hideturtle()
#거북이 숨기기
t.done()
#그림 다 그렸음을 알려줌