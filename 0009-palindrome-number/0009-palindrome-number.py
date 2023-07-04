class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        for original, reverse in zip(str(x), str(x)[::-1]):
            if original != reverse:
                return False
        else:
            return True