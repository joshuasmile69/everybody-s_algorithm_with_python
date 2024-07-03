#이제 친구 리스트를 기반으로 친밀도를 계산함
def friend_intimacy(a, b):
    #앞으로 처리해야 할 사람들의 위치
    queue=[]
    #이미 처리 완료된 사람들은 집합에 기록해서, 중복을 방지함
    done=set()

    #자신은 큐와 집합에 넣어서 이미 처리된 것 취급, 이때 튜플(tuple)을 이용하여 본인의 친밀도를 1로 설정
    queue.append((b, 1))
    done.add(b)

    while queue:
        #큐에 있는 첫번째 튜플을 꺼내서
        (p,d)=queue.pop(0)
        #출력하고
        print(p,d)
        #p(key)의 친구목록(value)에 있는 x들에 대해서
        for x in a[p]:
            #아직 처리가 안된 애라면(done에 없으면)
            if x not in done:
                #queue와 done에 추가하는데, 이 과정마다 다리 하나를 건너는 거니까 tuple의 2번째 항(친밀도)을 반으로 줄임
                queue.append((x,d/2))
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

friend_intimacy(friend_information, "Anastasia")