#1456-Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Set of vowel characters
        vowels = set('aeiou')
        
        # Calculate initial count of vowels in the first k characters
        t = sum(c in vowels for c in s[:k])
        
        # Initialize the maximum count
        ans = t

        # Iterate with a sliding window
        for i in range(k, len(s)):
            # Update the count for the current character
            t += s[i] in vowels
            
            # Update the count for the character out of the window
            t -= s[i - k] in vowels
            
            # Update the maximum count encountered so far
            ans = max(ans, t)

        # Return the maximum count of vowels
        return ans
