class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, _ in tickets}
        ans = []

        for src, dest in tickets:
            adj[src].append(dest)

        for key in adj:
            adj[key].sort()

        def dfs(adj, ans, src):
            if src in adj:
                destinations = adj[src]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, ans, dest)
                    destinations = adj[src][:]
            ans.append(src)                    

        dfs(adj, ans, "JFK")

        ans.reverse()

        if len(ans) != len(tickets) + 1:
            return []

        return ans