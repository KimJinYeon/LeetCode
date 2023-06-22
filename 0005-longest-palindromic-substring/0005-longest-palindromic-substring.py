class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_str = ""
        
        for i in range(len(s)):
            
            # 홀수 팰린드럼
            left_wing_odd = s[:i]
            right_wing_odd = s[i+1:]
            odd_count = 0
            
            for left, right in zip(left_wing_odd[::-1], right_wing_odd):
                if left != right:
                    break
                else:
                    odd_count += 1
            
            odd_length = odd_count * 2 + 1
            
            # 짝수 팰린드럼
            left_wing_even = s[:i+1]
            right_wing_even = s[i+1:]
            even_count = 0
            
            for left, right in zip(left_wing_even[::-1], right_wing_even):
                if left != right:
                    break
                else:
                    even_count += 1
            
            even_length = even_count * 2
        
            if len(longest_str) < odd_length:
                longest_str = s[i-odd_count:i+odd_count+1]
                print("odd")

            if len(longest_str) < even_length:
                longest_str = s[i-even_count+1:i+even_count+1]
                print("even")
        
        return longest_str