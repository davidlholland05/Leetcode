class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            stone1 = heapq.heappop(stones) * -1
            stone2 = heapq.heappop(stones) * -1

            smash = stone1 - stone2

            if smash:
                heapq.heappush(stones, -smash)

        return -stones[0] if stones else 0