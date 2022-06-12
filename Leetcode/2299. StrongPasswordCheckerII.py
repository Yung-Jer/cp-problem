class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        upper_flag = False
        lower_flag = False
        digit_flag = False
        special_flag = False
        repeat_flag = False
        len_flag = False
        n = len(password)
        if n >= 8:
            len_flag = True
        stack = []
        
        for i in range(n):
            if stack and password[i] == stack[-1]:
                repeat_flag = True
            stack.append(password[i])
            if password[i] in "!@#$%^&*()-+":
                special_flag = True
            elif password[i].isdigit():
                digit_flag = True
            elif password[i].isupper():
                upper_flag = True
            else:
                lower_flag = True
            
                
        ans = upper_flag and lower_flag and digit_flag and special_flag and len_flag and not repeat_flag
        return ans
        
        