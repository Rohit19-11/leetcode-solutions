# Problem: 3867. Sum of GCD of Formed Pairs
# Platform: LeetCode Biweekly Contest 178
# Difficulty: Medium
# Pattern: Array, Prefix Maximum, Sorting, Two Pointers, GCD
# Time Complexity: O(n log n)
# Space Complexity: O(n)
from math import gcd
from typing import List
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        curr_max  = 0
        for num in nums:
            curr_max = max(curr_max,num)
            prefix_gcd.append(gcd(num,curr_max))
        prefix_gcd.sort()
        left = 0
        right = len(prefix_gcd) - 1
        answer = 0
        while left < right:
            answer += gcd(prefix_gcd[left],prefix_gcd[right])
            left += 1
            right -= 1
        return answer
        
        