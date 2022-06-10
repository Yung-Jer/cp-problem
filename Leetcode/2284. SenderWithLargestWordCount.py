class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        dct = {}
        for i in range(len(messages)):
            if senders[i] not in dct:
                dct[senders[i]] = len(messages[i].split(" "))
            else:
                dct[senders[i]] += len(messages[i].split(" "))
        count = 0
        name = ""
        for i in dct:
            if dct[i] > count:
                count = dct[i]
                name = i
            elif dct[i] == count:
                if i > name:
                    name = i
        return name