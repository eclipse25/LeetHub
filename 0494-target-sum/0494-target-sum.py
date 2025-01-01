class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        dp[-nums[0]] = dp.get(-nums[0], 0) + 1
        dp[nums[0]] = dp.get(nums[0], 0) + 1

        for i in range(1, len(nums)):
            next_dp = {}
            for key, value in dp.items():
                sum1 = key + nums[i]
                sum2 = key - nums[i]

                next_dp[sum1] = next_dp.get(sum1, 0) + value
                next_dp[sum2] = next_dp.get(sum2, 0) + value

            dp = next_dp
        return dp.get(target, 0)