class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        if not tokens:
            return 0
        elif power < min(tokens):
            return 0
        tokens.sort()
        left = 0
        right = len(tokens)-1
        score = 0
        
        while left < right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            else:
                score -= 1
                power += tokens[right]
                right -= 1
        if power >= tokens[left]:
            score += 1
        return max(score, 0)