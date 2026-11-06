# Count Zero Request Servers
# Difficulty: Medium
# https://leetcode.com/problems/count-zero-request-servers/

# Sort logs and queries by time to enable a sliding window approach. Maintain a frequency map of servers within the current time window for each query to efficiently count unique servers.
import collections

class Solution:
    def countZeroRequestServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])
        
        queries_with_indices = sorted([(query_time, i) for i, query_time in enumerate(queries)])
        
        results = [0] * len(queries)
        
        server_request_counts = collections.Counter()
        
        left_log_pointer = 0