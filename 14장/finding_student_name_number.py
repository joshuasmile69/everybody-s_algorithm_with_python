#딕셔너리를 보고 학생 번호를 받으면 이름을 출력하는 알고리즘
def student_name_number(a, b):
    #딕셔너리(b)에 a(key)가 있는지 여부를 확인
    if b in a:
        return a[b]
    else:
        return "해당 번호는 빈 번호입니다"
    
student_number={13:"Anastasia", 15:"Franz", 18:"Tom", 6:"Eudokia", 3:"Clementia"}

print(student_name_number(student_number, 6))
print(student_name_number(student_number, 16))