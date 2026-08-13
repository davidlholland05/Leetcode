class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            half = (left + right) // 2

            if nums[half] == target:
                return half

           
            if nums[left] <= nums[half]:
                if nums[left] <= target < nums[half]:
                    right = half - 1
                else:
                    left = half + 1
          
            else:
                if nums[half] < target <= nums[right]:
                    left = half + 1
                else:
                    right = half - 1

        return -1