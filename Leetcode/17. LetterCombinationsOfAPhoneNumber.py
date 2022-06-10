class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        # Initialize mapping of digits to letters
        letter_dict = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz")
        }
        
        # Starting from an empty string, iterate through the digits
        # each possible mapping letter is added to the empty string
        # continue working on each string, iterate through the following
        # letters and do the same mapping
        combi = [""]
        for i in list(digits):
            temp = []
            for each in combi:
                for j in letter_dict[i]:
                    temp.append(each + j)
            combi = temp
        return combi