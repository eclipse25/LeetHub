class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:  # 길이가 홀수라면 유효하지 않음
            return False

        opening, closing, not_locked = 0, 0, 0
        for i in range(len(s)):
            if locked[i] == '0':
                not_locked += 1
            elif s[i] == '(':
                opening += 1
            else:
                closing += 1

            if not_locked < (closing - opening):
                return False

        opening, closing, not_locked = 0, 0, 0
        for i in range(len(s) - 1, -1, -1): 
            if locked[i] == '0':
                not_locked += 1
            elif s[i] == '(':
                opening += 1
            else:
                closing += 1

            # Overbalanced '(' check
            if not_locked < (opening - closing):
                return False

        return True
