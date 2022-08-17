class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        temp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = {chr(97 + i): temp[i] for i in range(26)}
        
        return len(set([''.join([mapping[key] for key in list(i)]) for i in words]))