class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        bin_data = list(map(lambda x: '{:08b}'.format(x), data))
        cur = 0
        while cur < len(data):
            if bin_data[cur].startswith('10'):
                return False
            n_bit = 0
            for i in range(8):
                if bin_data[cur][i] == '1':
                    n_bit += 1
                else:
                    break
            n_bit = max(n_bit, 1)
            if n_bit > 4:
                return False
            if cur + n_bit > len(data):
                return False
            for i in range(cur+1, cur+n_bit):
                if not bin_data[i].startswith('10'):
                    return False
                cur += 1
            cur += 1
        return True