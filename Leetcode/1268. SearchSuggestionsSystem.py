import bisect

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        res = []
        n = len(searchWord)
        start = 0
        
        for i in range(1,n+1):
            word = searchWord[:i]
            idx = bisect.bisect_left(products, word, lo=start)
            start = idx
            res.append([w for w in products[idx:idx+3] if w.startswith(word)])
        return res