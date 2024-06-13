class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d_map = [[] for i in range(numCourses)]
        visited, added = set(), set()
        ans = []

        for crs, dep in prerequisites:
            d_map[crs].append(dep)

        def dfs(crs):
            if crs in visited:
                return False

            if crs in added:
                return True

            visited.add(crs)
            for dep in d_map[crs]:
                if not dfs(dep):
                    return False

            visited.remove(crs)
            d_map[crs] = []
            added.add(crs)
            ans.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans

            