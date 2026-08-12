class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * (len(temperatures))
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                val0,val1 = stack.pop()
                
                answer[val1] = i-val1

            stack.append((temp,i))
        return answer



