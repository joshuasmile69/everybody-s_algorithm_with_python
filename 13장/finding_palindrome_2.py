#스택이나 큐 없이, 그냥 리스트 자체에서 회문 여부를 확인해보는 함수
def finding_palindrome_2(a):
    #정리해서 넣을 리스트 하나를 생성
    b=[]
    for x in a:
        #이때 집어넣는 것은 문자가 알파벳일 때로 한정
        if x.isalpha():
            #문자열 입력
            b.append(x.lower())
    #문자열의 중간까지에 대해서
    for i in range(0,(len(b)-1)//2):
        #문자열의 i번째와 길이-i번째 항이 같은지 여부를 확인
        if b[i] != b[len(b)-1-i]:
            #다른 경우가 있다면 회문이 아님
            return ("the sentence is not a palindrome")
    #다 통과한거라면, 회문임이 확인된 것
    return ("the sentence is a palindrome")

print(finding_palindrome_2("wow, god dog! wow!"))
print(finding_palindrome_2("소주 만병만 주소"))
print(finding_palindrome_2("this is not a palindrome"))