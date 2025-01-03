class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        left, right = 0, sum(nums)
        for i in range(0, len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                answer += 1

        return answer