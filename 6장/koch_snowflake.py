#코흐 눈송이 알고리즘
import turtle as t

def koch_snowflake(snowflake_length):
#변수: 눈송이(선분)의 길이
    if snowflake_length<=10:
        #선분의 길이가 10보다 작으면(종료조건)
        t.forward(snowflake_length)
        #선분 길이만큼 선을 긋고
        return
        #종료(return)
    new_length=snowflake_length/3
    #원래 길이의 1/3으로 길이를 재정의
    koch_snowflake(new_length)
    #새로운 길이를 기준으로 함수를 호출(재귀)
    t.left(60)
    #60도 왼쪽으로 꺾어서
    koch_snowflake(new_length)
    #새로운 길이를 기준으로 함수를 호출(재귀)
    t.right(120)
    #오른쪽으로 120도 꺾어서
    koch_snowflake(new_length)
    #새로운 길이를 기준으로 함수를 호출(재귀)
    t.left(60)
    #다시 60도 왼쪽으로 꺾어서
    koch_snowflake(new_length)
    #새로운 길이를 기준으로 함수를 호출(재귀)

t.speed(0)
koch_snowflake(200)
t.right(120)
koch_snowflake(200)
t.right(120)
koch_snowflake(200)
t.hideturtle()
t.done()