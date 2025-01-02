class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                nums.append(1)
            else:
                nums.append(0)
        
        ans = []
        prefix_sum = [0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            prefix_sum.append(temp)

        for query in queries:
            answer = prefix_sum[query[1] + 1] - prefix_sum[query[0]]
            ans.append(answer)

        return ans