class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 'abcdefghijklmnopqrstuvwxyz0123456789'
        x = ""
        for i in s.lower():
            if i in a:
                x += i
        return x == x[::-1]

