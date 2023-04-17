def dfs(graph:dict, start:str):
    visited = {i : False for i in graph.keys()}
    
    stack = [start]
    visited[start] = True
    

    while stack:
        current = stack.pop()

        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')