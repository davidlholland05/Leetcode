class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = Counter()

        longest = 0
        left=0

        for right, i in enumerate(s):

            counts[i] += 1

            while counts[i] > 1:
                counts[s[left]] -= 1
                left += 1

            longest =  max(longest, right - left + 1)
            
        return longest

