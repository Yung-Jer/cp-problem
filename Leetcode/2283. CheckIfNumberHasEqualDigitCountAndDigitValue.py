class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dct = {}
        for i in range(len(num)):
            if num[i] not in dct:
                dct[num[i]] = 1
            else:
                dct[num[i]] += 1
                
        for i in range(len(num)):
            if str(i) not in dct:
                dct[str(i)] = 0
        flag = True
        for i in range(len(num)):
            if dct.get(str(i), -1) != int(num[i]):
                flag = False
                break
        return flag