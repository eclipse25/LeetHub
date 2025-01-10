class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        required = {}
        answer = []
        for word in words2:
            for char in word:
                required[char] = max(required.get(char, 0), word.count(char))
        for word in words1:
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1

            is_universal = True
            for char, count in required.items():
                if word_count.get(char, 0) < count:
                    is_universal = False
                    break

            if is_universal:
                answer.append(word)
        
        return answer