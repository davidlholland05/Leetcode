class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set(nums)
        
        return len(nums) != len(hash)