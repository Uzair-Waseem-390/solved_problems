# Restore IP Addresses
# Difficulty: Medium
# https://leetcode.com/problems/restore-ip-addresses/

# Backtracking approach: recursively try to build 4 segments, validating each segment for length, leading zeros, and value range (0-255).

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        results = []
        n = len(s)

        def backtrack(start_index: int, num_segments_formed: int, current_ip_parts: list[str]):
            # Base case 1: Formed exactly 4 segments
            if num_segments_formed == 4:
                # If all characters from the input string have been used, it's a valid IP
                if start_index == n:
                    results.append(".".join(current_ip_