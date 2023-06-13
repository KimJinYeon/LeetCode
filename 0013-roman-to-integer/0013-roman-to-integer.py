class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        for i in range(len(s)-1):
            current_num = roman_to_int.get(s[i])
            next_num = roman_to_int.get(s[i+1])
            if current_num < next_num:
                count -= current_num
            else:
                count += current_num
        else:
            count += roman_to_int.get(s[-1])

        return count
