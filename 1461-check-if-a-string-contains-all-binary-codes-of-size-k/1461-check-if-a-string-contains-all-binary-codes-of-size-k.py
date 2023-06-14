class Solution:
    
    def binary_convert(self, binary_str):
        decimal = 0
        digit = 0
        for char in binary_str[::-1]:
            decimal += int(char) * pow(2, digit)
            digit += 1

        return decimal
    
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_candidates = dict()
        
        for i in range(len(s) - k + 1):
            binary_candidates[self.binary_convert(s[i:i+k])] = True
        
        for i in range(self.binary_convert("1" * k) + 1):
            if i not in binary_candidates:
                return False
        else:
            return True
    
