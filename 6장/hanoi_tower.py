#하노이의 탑 알고리즘
def hanoi_tower(a, start_pillar, end_pillar, support_pillar):
#하노이의 탑에 필요한 변수 1) 옮기는 원반의 개수(a) 2) 시작하는 기둥(start_pillar) 3) 목적지 기둥(end_pillar) 4) 보조 기둥(support_pillar)
    if a==1:
    #하노이의 탑이 하나라면(종료조건)
        print(start_pillar, "->", end_pillar)
        #시작하는 기둥에서 목적지 기둥으로 옮기는 것으로 끝남
        return
        #추가사항 없이 return
    hanoi_tower(a-1, start_pillar, support_pillar, end_pillar)
    #그 외의 경우, 우선 a-1개의 원반을 시작하는 기둥에서 보조 기둥으로 옮기고(재귀)
    print(start_pillar, "->", end_pillar)
    #가장 큰 원반을 목적지 기둥으로 옮긴 후
    hanoi_tower(a-1, support_pillar, end_pillar, start_pillar)
    #다시 a-1개의 원반을 보조 기둥에서 목적지 기둥으로 옮김(재귀)
    #어차피 이를 반복하면 a=1일 때 return하니까 굳이 따로 return을 안써줌

print("a=5")
hanoi_tower(5, 1, 3, 2)