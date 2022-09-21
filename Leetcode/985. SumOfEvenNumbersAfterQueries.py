class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_sum = sum([i for i in nums if i % 2 == 0])
        res = []
        
        for query in queries:
            num = nums[query[1]]
            is_even = num % 2 == 0
            if is_even:
                even_sum -= num
            nums[query[1]] = num + query[0]
            if (num + query[0]) % 2 == 0:
                even_sum += (num + query[0])
            res.append(even_sum)
        return res