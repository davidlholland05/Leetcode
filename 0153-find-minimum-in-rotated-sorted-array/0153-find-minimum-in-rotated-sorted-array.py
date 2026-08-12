class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            half = (left+right)//2

           
            if nums[half] > nums[right]:
                left = half+1
            else:
                right = half 

        return nums[left]
 

        