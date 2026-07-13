class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        finalList = []

        for i in range(k):
            finalList.append(freq[i][0])

        return finalList