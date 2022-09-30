class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        return sorted(sorted(arr, key=lambda y: abs(y-x))[:k])