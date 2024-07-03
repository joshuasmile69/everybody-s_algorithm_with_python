#친구의 친구들까지 전부 포함해서 연결되어 있는 사람들 전부 찾기 알고리즘
#dictionary를 이용해서 친구 관계를 표현하고, 이를 그래프(graph)라고 부를 것

def friends_friend(a, b):
    #앞으로 처리해야 할 사람들의 위치
    queue=[]
    #이미 처리 완료된 사람들은 집합에 기록해서, 중복을 방지함
    done=set()

    #자신은 큐와 집합에 넣어서 이미 처리된 것 취급
    queue.append(b)
    done.add(b)
    #큐가 비어있지 않으면
    while queue:
        #큐에서 하나(맨 앞)을 꺼내서
        p=queue.pop(0)
        #출력하고
        print(p)
        #a[p], 즉 이 경우 p(key)의 친구목록(value)에 해당하는 값을 확인해서
        for x in a[p]:
            #아직 처리가 안된 사람이면 queue랑 done에 추가
            #(이러면 아직까지 출력 안된 사람은 출력될거고, 이미 출력된 사람은 done에 있으므로 생략됨)
            if x not in done:
                queue.append(x)
                done.add(x)

friend_information={
    "Anastasia":["Franz", "Tom", "Eudokia"],
    "Franz":["Tom", "Anastasia"],
    "Tom":["Franz", "Tom", "Anastasia", "Harold"],
    "Eudokia":["Anastasia", "Clementia"],
    "Clementia":["Eudokia", "Harold"],
    "Harold":["Tom", "Clementia"],
    "Blanche":["Alexander"],
    "Alexander":["Blanche"]}

friends_friend(friend_information, "Anastasia")
print()
friends_friend(friend_information, "Blanche")