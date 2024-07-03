#미로 탐색 알고리즘
#미로를 구획으로 나눠서, 일종의 그래프와 같이 해석, 도착하는 경로를 일련의 문자열로 표현해본다.
#미로는 5*5짜리로 만들어본다(그림은 나중에 궁금하면 만들어보면 된다)
#근본적으로 적용하는 알고리즘은 15장의 너비 우선 탐색(breadth first search)과 동일하므로,
#여러 경로가 존재한다면 가장 거쳐가는 구획이 적은 문자열을 출력하게 될 것이다.
def labyrinth_solving(graph, start, end):
    queue=[]
    done=set()
    queue.append(start)
    done.add(start)
    while queue:
        p=queue.pop(0)
        #현재 위치=문자열의 마지막 지점이므로 v=p[-1]로 놓는다.
        v=p[-1]
        #목표 지점에 도달했다면 문자열 p를 제시하고
        if v==end:
            return p
        #도달하지 못했다면, 해당 그래프에 연결되어 있는 경로들 중
        for x in graph[v]:
            #아직 지나가지 않은 위치들에 대하여(지나간 경로를 중복해서 움직이지 않게 한다)
            if x not in done:
                #문자열 뒤에 붙여 다음 위치로 이동함을 표시하고, done에 추가해두어서 중복을 방지한다
                queue.append(p+x)
                done.add(x)
    return "탈출구가 없는 미로입니다"

#미로는 각 구획당 연결된(즉 막혀있지 않은) 구획들 간의 딕셔너리로서 표현이 가능한 셈이다
labyrinth={"a":["f"],
           "b":["c","g"],
           "c":["b","d"],
           "d":["c","e"],
           "e":["d","j"],
           "f":["k"],
           "g":["b","h"],
           "h":["m","i","g"],
           "i":["h"],
           "j":["e","o"],
           "k":["f","l"],
           "l":["m","k","q"],
           "m":["l","h"],
           "n":["o"],
           "o":["n","j","t"],
           "p":["u","q"],
           "q":["p","r","l","v"],
           "r":["q","s"],
           "s":["r","x"],
           "t":["o","y"],
           "u":["p"],
           "v":["q"],
           "w":["x"],
           "x":["w","s"],
           "y":["t"]}

print(labyrinth_solving(labyrinth, "a", "y"))