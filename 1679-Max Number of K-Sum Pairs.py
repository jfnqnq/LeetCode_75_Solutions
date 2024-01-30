#1679-Max Number of K-Sum Pairs



class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_freq = {}  # Dictionary to store the frequency of each number
        ans = 0  # Initialize the count of operations

        # Iterate through the array to find pairs that sum up to k
        for num in nums:
            complement = k - num

            # Check if the complement exists in the dictionary and has a positive frequency
            if complement in num_freq and num_freq[complement] > 0:
                # Increment the count of operations
                ans += 1

                # Reduce the frequency of the complement in the dictionary
                num_freq[complement] -= 1
            else:
                # Increment the frequency of the current number in the dictionary
                if num not in num_freq:
                    num_freq[num] = 0
                num_freq[num] += 1

        return ans

