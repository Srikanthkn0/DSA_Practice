class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak,cnt=0,num
            while cnt in nums:
                streak += 1
                cnt += 1
            res = max(streak , res)
        return res        