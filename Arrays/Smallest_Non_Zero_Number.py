# Problem: Smallest Non-Zero Number
# Platform: GeeksforGeeks
# Difficulty: Medium
# Pattern: Arrays, Binary Search
# Time Complexity: O(n log M)
# Space Complexity: O(1)
class Solution:
    def find(self, arr):
        required = 0

        for i in range(len(arr) - 1, -1, -1):
            required = (required + arr[i] + 1) // 2

        return required