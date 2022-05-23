class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        counter = [(i.count("0"), i.count("1")) for i in strs]
        dct = {}
        
        def recur(m, n, curr_idx):
            if (m,n,curr_idx) in dct:
                return dct[(m,n,curr_idx)]
            elif m < 0 or n < 0:
                return -100 #just a dummy value
            elif curr_idx >= len(strs):
                return 0
            else:
                dct[(m, n, curr_idx+1)] = recur(m, n, curr_idx+1)
                dct[(m-counter[curr_idx][0], n-counter[curr_idx][1], curr_idx+1)] = recur(m-counter[curr_idx][0], n-counter[curr_idx][1], curr_idx+1)
                return max(recur(m, n, curr_idx+1), 1+recur(m-counter[curr_idx][0], n-counter[curr_idx][1], curr_idx+1))
        return recur(m,n,0)