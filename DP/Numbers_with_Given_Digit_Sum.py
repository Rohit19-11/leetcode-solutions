# Problem: Numbers with Given Digit Sum
# Platform: GeeksForGeeks
# Pattern: Dynamic Programming, Counting DP
# Time Complexity: O(n × Sum)
# Space Complexity: O(n × Sum)
class Solution:
    def countWays(self, n, sum):
        if sum < 1 or sum > 9 * n:
            return -1
        dp = [[0] * (sum + 1) for _ in  range(n + 1)]
        for digit in range(1,10):
            if digit <= sum:
                dp[1][digit] = 1
        for  position in range(2, n+1):
            for current_sum in range(sum + 1):
                for digit in range (10):
                    if current_sum >= digit:
                        dp[position][current_sum] += dp[position - 1][current_sum - digit]
        answer = dp[n][sum]
        return answer if answer > 0 else -1