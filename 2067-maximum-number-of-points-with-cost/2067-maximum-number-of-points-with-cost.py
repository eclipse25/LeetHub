class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = points[0]
        
        for i in range(1, m):
            # 현재 행의 dp 배열
            curr = [0] * n
            
            # 왼쪽에서부터 최대값 계산
            left_max = [0] * n
            left_max[0] = prev[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j - 1], prev[j] + j)

            # 오른쪽에서부터 최대값 계산
            right_max = [0] * n
            right_max[n - 1] = prev[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                right_max[j] = max(right_max[j + 1], prev[j] - j)

            # 현재 dp 계산
            for j in range(n):
                curr[j] = points[i][j] + max(left_max[j] - j, right_max[j] + j)
            
            prev = curr
        
        return max(prev)


