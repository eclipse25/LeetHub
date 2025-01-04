from collections import defaultdict

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        positions = defaultdict(list)
        for i in range(len(s)):
            positions[s[i]].append(i)
        
        palindromes = set()
        for key, value in positions.items():
            if len(value) < 2:
                continue
            
            left = value[0]
            right = value[-1]
            if right > left + 1:
                middles = set(s[left + 1: right])
                for char in middles:
                    palindromes.add((key, char))

        return len(palindromes)