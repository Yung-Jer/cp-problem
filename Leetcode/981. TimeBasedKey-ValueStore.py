from sortedcontainers import SortedList
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.containers = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None: # Sort by timestamp, then value
        self.containers[key].add((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        idx = self.containers[key].bisect_left((timestamp, "|")) # | is larger than all english letters in ASCII values
        return self.containers[key][idx - 1][1] if idx != 0 else ""