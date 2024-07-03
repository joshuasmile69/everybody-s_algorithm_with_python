#동명이인 찾기 알고리즘을 딕셔너리(dictionary) 개념을 이용하여 해보기
#dictionary는 key를 기준으로 key에 연결된 value를 저장함
def find_same_name_dictionary(a):
    #우선 이름 별 등장 횟수를 지정할 딕셔너리 생성
    name_count={}
    #a에 있는 이름들에 대해서
    for name in a:
        #name_count 딕셔너리에 이미 이름이 존재한다면
        if name in name_count:
            #해당 이름(key)에 해당하는 횟수(value)를 +1
            name_count[name] += 1
        #아닐 경우 이름(key)을 추가하고 등장 횟수(value)에 1을 부여
        else:
            name_count[name]=1
    #이 다음으로 동명이인 목록을 저장할 집합을 생성
    result=set()
    for name in name_count:
        #이름의 등장 횟수(value)가 2 이상인 이름(key)들에 대해
        if name_count[name]>=2:
            #해당 이름(key)들을 집합에 추가
            result.add(name)
    return result

#틀렸던 것: 주의사항! 대괄호/중괄호/소괄호 틀리면 names의 성격이 달라져서 작동 오류남!
names=["Anastasia", "Franz", "Tom", "Eudokia", "Clementia", "Harold", "Richard", "Blanche", "Alexander", "Richard", "Raynold", "Anna", "Patricia", "Anna", "Franz", "Nancy"]
print(find_same_name_dictionary(names))