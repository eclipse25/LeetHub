class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                groups.append(cnt)
                cnt = 1
        groups.append(cnt)
        
        answer = 0
        for i in range(len(groups) - 1):
            answer += min(groups[i], groups[i + 1])
        
        return answer