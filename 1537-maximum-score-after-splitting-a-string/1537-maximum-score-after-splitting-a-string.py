class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers = list(map(int, s))
        left = 1 if numbers[0] == 0 else 0
        right = sum(numbers[1:])
        answer = left + right
        for i in range(1, len(numbers) - 1):
            if numbers[i]:
                right -= 1
            else:
                left += 1
            answer = max(answer, left + right)

        return answer
