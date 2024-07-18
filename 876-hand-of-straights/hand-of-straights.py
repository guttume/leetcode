class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = {}
        for num in hand:
            counter[num] = 1 + counter.get(num, 0)

        minH = list(counter.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1

                if counter[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)
                
        return True
