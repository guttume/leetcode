class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        q = collections.deque()
        pq = []

        for value in count.values():
            heapq.heappush(pq, -1 * value)

        timer = 0

        while pq or q:
            timer += 1

            if q and q[0][1] == timer:
                task, _ = q.popleft()
                heapq.heappush(pq, -1 * task)

            if pq:
                task = heapq.heappop(pq) * -1
                task -= 1
                if task > 0:
                    q.append((task, timer + n + 1))

        return timer

