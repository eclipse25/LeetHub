class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        indexes = []
        for char in s:
            indexes.append(ord(char) - 97)

        count = [0]  * (len(s) + 1)
        for shift in shifts:
            direction = 1 if shift[2] == 1 else -1
            count[shift[0]] += direction
            count[shift[1] + 1] -= direction
        
        pre_sum = 0
        answer = ""
        for i in range(len(indexes)):
            pre_sum += count[i]
            new_char = chr((indexes[i] + pre_sum) % 26 + 97)
            answer += new_char
            
        return answer