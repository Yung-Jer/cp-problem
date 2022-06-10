class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        string_arr = sentence.split(' ')
        
        for i in range(len(string_arr)):
            if string_arr[i][0] == '$' and len(string_arr[i]) > 1 and string_arr[i][1:].isdigit():
                amount = float(string_arr[i][1:])
                amount = "{:.2f}".format(amount * (100 - discount) / 100)
                string_arr[i] = '$' + str(amount)
        return ' '.join(string_arr)
                