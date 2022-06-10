import bisect 

class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        # first sort all tiles by the start
        sorted_tiles = sorted(tiles, key=lambda x: x[0])
        
        # initialize prefix sum array
        prefix_sum = [0] * (len(tiles)+1)
        
        starts, ends = zip(*sorted_tiles)
        max_cover = 0
        
        # fill in the value of each cumulative prefix array
        for i in range(len(tiles)):
            prefix_sum[i+1] = prefix_sum[i] + (ends[i]-starts[i]+1)
        
        for left in range(len(tiles)):
            # find where is the end of the carpet if the carpet is placed at the start of the tile
            end = starts[left] + carpetLen - 1
            right = bisect.bisect_right(starts, end)
            
            # end might be larger than ends[right-1] as where the carpet ends might be after the end of the tile 
            num_cover = prefix_sum[right] - prefix_sum[left] - max(0, ends[right-1] - end) 
            print(end, left, right, num_cover)
            max_cover = max(num_cover, max_cover)
        
        return max_cover