class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        top = 0

        for num in seen:
            if num - 1 in seen:
                continue
            length = 1
            while num + length in seen:
                length += 1
            
            top = max(top, length)
        
        return top

