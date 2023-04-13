from collections import deque

# Dict 자료형 형태로 준다. key는 노드, value는 인접노드를 가리킨다.
def bfs(graph:dict, start:int):
    visited = {i:False for i in graph.keys()} # 방문 배열. visited[node] = True이면 node는 방문이 끝난 상태이다.
    queue = deque([start])

    visited[start] = True

    # 큐가 빌 때까지 반복
    while len(queue) > 0:
        current = queue.popleft() #queue에서 노드를 하나 빼 온다. 이 노드를 current라고 하자.
        
        # current의 인접 노드들을 확인한다. 이 각각의 노드를 nxt라고 하자.
        for nxt in graph[current]:
            # 만일 nxt에 방문하지 않았다면
            if not visited[nxt]:
                #nxt 방문
                queue.append(nxt)
                visited[nxt] = True

                print(nxt)

# TEST

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')