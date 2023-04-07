def testDfs(graph, v, visited):
    stack = list()

    while(len(stack) < (len(graph) - 1)):
        print(v, end = " ")

        for nowNode in graph[v]:
            if(not visited[nowNode]):
                visited[v] = True
                break
        
        stack.append(nowNode)
        v = nowNode

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

testDfs(graph, 1, visited)