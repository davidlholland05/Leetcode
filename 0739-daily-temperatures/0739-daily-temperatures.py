class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * (len(temperatures))
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                val0,val1 = stack.pop()
                index = i-val1
                answer[val1] = index

            stack.append((temp,i))
        return answer



