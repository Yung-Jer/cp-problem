class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        def match(s1, s2):
            if s1 == "?" * len(s1):
                return False
            s1, s2 = list(s1), list(s2)
            for i in range(len(s1)):
                if s1[i] != "?" and s1[i] != s2[i]:
                    return False
            return True
        
        m, n = len(target), len(stamp)
        log = []
        temp = target
        
        for _ in range(10 * m):
            if temp == "?" * m:
                break
            flag = -1
            for i in range(m - n + 1):
                if match(temp[i:i+n], stamp):
                    flag = i
                    break
            if flag == -1:
                return []
            temp = temp[:flag] + '?' * n + temp[flag+n:]
            log.append(flag)
            
        return log[::-1] if temp == "?" * m else []