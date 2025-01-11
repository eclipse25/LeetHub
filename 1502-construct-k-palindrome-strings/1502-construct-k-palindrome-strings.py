class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
            
        count = collections.Counter(s)
        odd = 0
        for value in count.values():
            if value % 2 != 0:
                odd += 1
                if odd > k:
                    return False
        return True