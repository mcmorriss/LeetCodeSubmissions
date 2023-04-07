class Solution:
    def removeVowels(self, s: str) -> str:

        s = list(s)
        p1, p2 = 0, len(s) - 1
        vowels = {'a','e','i','o','u'}

        while p1 < p2:
            if s[p2] in vowels:
                s.pop(p2)
                p2 -= 1

            if s[p1] in vowels:
                s.pop(p1)
                p2 -= 1
            else:
                p1 += 1
        if len(s) == 1 and s[0] in vowels:
            s.pop()

        return "".join(s)
