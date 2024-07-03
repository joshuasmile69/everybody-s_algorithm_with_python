#배운 걸 기반으로, 그래프 탐색 알고리즘을 적어본다
#적는 탐색 알고리즘은 너비 우선 탐색 알고리즘(breadth first search algorithm)이다
#그래프는 딕셔너리 형태로 적으면 알아보기 어려울 수 있지만, 딕셔너리를 직접 그림으로 그려본다면 금방 이해가 간다.

#방식은 친구의 친구 찾기 알고리즘과 생긴 게 똑같다! 다시말해서 사실 우리의 친구의 친구 찾기 알고리즘은 너비 우선 탐색 알고리즘을 적용한 사례이다
#큐를 사용하고 있기 때문에 먼저 들어간 게 먼저 처리되므로(fifo),
#같은 깊이에 있는 값이 들어온 다음 그 아래 깊이에서 탐색된 값이 들어오기 때문에,
#깊이가 아니라 너비를 기준으로 하는 탐색(breadth first search)가 된다
def breadth_first_search(g, start):
    queue=[]
    done=set()
    queue.append(start)
    done.add(start)
    while queue:
        p=queue.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                queue.append(x)
                done.add(x)

graph={1:[2,3],
       2:[1,4,5],
       3:[1],
       4:[2],
       5:[2]}
breadth_first_search(graph,1)
breadth_first_search(graph,4)