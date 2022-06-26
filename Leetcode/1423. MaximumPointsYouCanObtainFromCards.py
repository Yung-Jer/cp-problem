class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k - 1
        window_sum = 0
        total_sum = sum(cardPoints)

        for i in range(left, right+1):
            window_sum += cardPoints[i]
        ans = total_sum - window_sum
        
        for i in range(right+1, len(cardPoints)):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[left]
            left += 1
            ans = max(ans, total_sum - window_sum)
        return ans