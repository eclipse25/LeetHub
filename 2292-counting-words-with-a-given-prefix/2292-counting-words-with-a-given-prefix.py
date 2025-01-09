class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        answer = 0
        for word in words:
            answer += 1 if word.startswith(pref) else 0
        
        return answer
            