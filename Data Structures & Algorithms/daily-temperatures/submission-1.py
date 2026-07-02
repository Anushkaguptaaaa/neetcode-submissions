class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        result = [0]* len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]]< temp[i]:
                ind = stack.pop()
                result[ind] = i - ind
            stack.append(i)
        return result
        