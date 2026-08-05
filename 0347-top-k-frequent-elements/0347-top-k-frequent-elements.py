class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        mh = []

        for key, val in freq.items():
            heapq.heappush(mh, (-val,key))

        res = []

        while k:
            k-=1
            res.append(heapq.heappop(mh)[1])

        return res
