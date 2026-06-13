class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        print(graph)
        i=0
        visited = set()
        path = set()
        
        def dfs(i):
            
            if i in path:
                return False
            if i in visited:
                return True
            path.add(i)
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            path.remove(i)
            visited.add(i)   
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        

