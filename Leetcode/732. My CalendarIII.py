import bisect

class MyCalendarThree:

    def __init__(self):
        self.start = []
        self.end = []

    def book(self, start: int, end: int) -> int:
        bisect.insort_right(self.start, start)
        bisect.insort_right(self.end, end)
        
        ans = -1
        for i in range(len(self.end)):
            idx = bisect.bisect_left(self.start, self.end[i])
            ans = max(ans, idx - i)
        return ans