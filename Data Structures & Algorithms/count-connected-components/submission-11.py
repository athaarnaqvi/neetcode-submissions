class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = 0
        visited = set()
        graph = [[] for _ in range(n)]


        for to,fro in edges:
            graph[to].append(fro)
            graph[fro].append(to)
        
        print (graph)

        def dfs(i):
            if i in visited:
                return
            visited.add(i)

            for neigh in graph[i]:
                dfs(neigh)
        

        for i in range(n):
            if i in visited:
                continue
            else:
                comp += 1
                dfs(i)

        return comp