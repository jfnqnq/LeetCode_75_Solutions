#1431- Kids with the greatest number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    mx = max(candies)
    return (candy + extraCandies >= mx for candy in candies)
