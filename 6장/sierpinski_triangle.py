#시에르핀스키 삼각형 알고리즘
#그림을 그려주는 turtle graphic을 import
import turtle as t

# 변수: 해당 선의 길이
def sierpinski_triangle(triangle_length):
        #길이가 10보다 작으면(종료조건)
        if triangle_length<=10:
            #i=0에서 2까지(즉 총 3번)
            for i in range(0, 3):
                #앞으로 가고 120도 회전해서 삼각형을 그림
                t.forward(triangle_length)
                t.left(120)
            return
        #원래 삼각형 길이의 절반을 정의
        new_length = triangle_length / 2
        #해당 길이를 가지고 다시 시에르핀스키 삼각형을 그림(재귀)
        sierpinski_triangle(new_length)
        #앞으로 가서 또다른 삼각형 그릴 준비
        t.forward(new_length)
        #해당 길이를 가지고 다시 시에르핀스키 삼각형을 그림(재귀)
        sierpinski_triangle(new_length)
        #아직 안 그린 삼각형 그림 그릴 시작점으로 이동
        t.backward(new_length)
        t.left(60)
        t.forward(new_length)
        t.right(60)
        #해당 길이를 가지고 다시 시에르핀스키 삼각형을 그림(재귀)
        sierpinski_triangle(new_length)
        # 다음 차의 시에르핀스키 그림을 그리게 이동
        t.left(60)
        t.backward(new_length)
        t.right(60)

#그림 그리는 속도 조절(이게 제일 빠른듯)
t.speed(0)
#초기 길이 설정
sierpinski_triangle(200)
#거북이 숨기기
t.hideturtle()
#그림 다 그렸음을 알려줌
t.done()