class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]

        for to, fro in edges:
            graph[to].append(fro)
            graph[fro].append(to)
        print(graph)
        visited= set()

        def dfs(node,parent):
            
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh,node):
                    return False
            return True
        

        if not dfs(0,-1):
            return False
        if len(visited) != n:
            return False
               
        return True

        

            
                