class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            target_word = s[i:]
            word_check = dict()
            for char in target_word:
                if char in word_check:
                        break
                word_check[char] = True
            longest = max(longest, len(word_check))
        return longest
                