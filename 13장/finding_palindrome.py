#회문 찾기 알고리즘
#큐(queue)와 스택(stack)에 대한 개념을 이해해보는 것이 부가적 목표
#queue는 fifo, 즉 선입선출 구조인데 stack은 lifo, 즉 후입선출 구조를 띔

#회문은 큐로 확인하든 스택으로 확인하든 동일한 결괏값을 출력하게 됨
def finding_palindrome(a):
    #우선 큐와 스택을 리스트를 이용하여 정의
    queue=[]
    stack=[]
    #확인할 문자열을 큐와 스택에 집어넣기
    for x in a:
        #이때 집어넣는 것은 문자가 알파벳일 때로 한정
        if x.isalpha():
            #큐와 스택에 각각 문자열 입력
            queue.append(x.lower())
            stack.append(x.lower())
    #큐가 빌 때까지
    while queue:
        #큐의 첫 글자와 스택의 마지막 글자를 가져와서 비교해봄
        if queue.pop(0) != stack.pop():
            #다른 경우가 있다면 회문이 아님
            return ("the sentence is not a palindrome")
    #다 통과한거라면, 회문임이 확인된 것
    return ("the sentence is a palindrome")

print(finding_palindrome("wow, god dog! wow!"))
print(finding_palindrome("소주 만병만 주소"))
print(finding_palindrome("this is not a palindrome"))