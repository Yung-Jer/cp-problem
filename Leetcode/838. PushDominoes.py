class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while temp != dominoes:
            temp = dominoes
            dominoes = dominoes.replace('R.L', '###')
            dominoes = dominoes.replace('.L', 'LL')
            dominoes = dominoes.replace('R.', 'RR')
        
        return dominoes.replace('###', 'R.L')