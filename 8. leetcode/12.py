class Solution:
    def intToRoman(self, num: int) -> str:
        
        IntRoman = collections.namedtuple('IntRoman', ['Int', 'Roman'])
        
        mapping = [IntRoman(1000, 'M'), 
             IntRoman(900, 'CM'), 
             IntRoman(500, 'D'),
             IntRoman(400, 'CD'),
             IntRoman(100, 'C'),
             IntRoman(90, 'XC'),
             IntRoman(50, 'L'),
             IntRoman(40, 'XL'),
             IntRoman(10, 'X'),
             IntRoman(9, 'IX'),
             IntRoman(5, 'V'),
             IntRoman(4, 'IV'),
             IntRoman(1, 'I')
            ]
        
        pos = 0
        
        res = []
        
        while num > 0:
            
            while num >= mapping[pos].Int:
                
                res.append(mapping[pos].Roman)
                num -= mapping[pos].Int
                
            pos += 1
            
        return ''.join(res)
        