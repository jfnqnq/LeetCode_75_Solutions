#345- Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str)->str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        i,j=0, len(s) -1
        chars = list(s)
        while i < j:
            if chars[i] not in vowels:
                i +=1
            elif char[j] not in vowels:
                j -=1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -=1
        return ''.join(chars)
            
        
        
