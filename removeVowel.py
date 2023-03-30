class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = 'aeiou'
        x = 0
        new = ""
        while x < len(s):
            if s[x] not in vowels:
                new += s[x]
            x += 1
        return new
