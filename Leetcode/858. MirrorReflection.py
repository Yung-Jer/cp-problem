import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = math.lcm(p, q)
        if (lcm // q) % 2 == 0: # even no. of rooms required to reach the receptor
            return 2
        # odd no. of rooms required to reach the receptor
        
        # if (lcm // p) % 2 == 0: the ray wil reach the bottom right receptor
        # else: the ray wil reach the top right receptor
        return (lcm // p) % 2