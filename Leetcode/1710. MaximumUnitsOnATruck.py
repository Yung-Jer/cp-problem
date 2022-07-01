class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        res = 0
        
        for box in boxTypes:
            if box[0] <= truckSize:
                truckSize -= box[0]
                res += box[0] * box[1]
            else:
                res += truckSize * box[1]
                break
        return res