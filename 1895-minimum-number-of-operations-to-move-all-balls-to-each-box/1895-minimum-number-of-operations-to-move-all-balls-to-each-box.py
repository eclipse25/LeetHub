class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ans = 0
        left, right = 0, 0
        length = len(boxes)
        for i, v in enumerate(boxes):
            if v == '1':
                ans += i
                if i > 0:
                    right += 1

        print(left, right)
        answer = [ans]
        for i in range(1, length):
            if boxes[i] == '1':
                ans -= 1
                right -= 1
            if boxes[i - 1] == '1':
                left += 1
            ans -= right
            ans += left
            answer.append(ans)

        return answer
        