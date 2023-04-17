def dfs(graph:dict, start:str):
    visited = {i : False for i in graph.keys()}

    stack = [start]
    visited[start] = True
                 
    while stack:
        judg = True
        current = stack[-1]

        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                judg = False
                break

        if judg:
            stack.pop()

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')