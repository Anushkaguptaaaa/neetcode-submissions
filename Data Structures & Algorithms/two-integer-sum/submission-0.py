class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}   # dictionary to store value:index

        for i, n in enumerate(nums):   # loop through array with index i and value n
            diff = target - n          # we need diff + n = target
            if diff in prevMap:        # if we have already seen diff earlier
                return [prevMap[diff], i]  # return its index and current index
            prevMap[n] = i             # otherwise store current number and index
        return
