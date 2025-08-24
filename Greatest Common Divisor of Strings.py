# Greatest Common Divisor of Strings

class Solutions(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""   # not compatible, no gcd string

        if len(str1) == len(str2):
            return str1  # equal length, must be answer

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        return self.gcdOfStrings(str1, str2[len(str1):])

    
sol = Solutions()
print(sol.gcdOfStrings('ABABAB','AB'))
print(sol.gcdOfStrings('ABCABC','ABC'))
