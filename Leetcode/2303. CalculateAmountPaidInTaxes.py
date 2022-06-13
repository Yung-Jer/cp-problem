class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        prefix, tax = zip(*brackets)
        i = 0
        prev = 0
        ans = 0
        
        while income > prefix[i]:
            diff = prefix[i] - prev
            ans += diff * tax[i] / 100
            prev = prefix[i]
            i += 1

        diff = income - prev
        ans += diff * tax[i] / 100
        return ans