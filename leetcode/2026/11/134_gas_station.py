# Gas Station
# Difficulty: Medium
# https://leetcode.com/problems/gas-station/

# The problem can be solved with a greedy approach.
# First, check if the total gas available is less than the total cost required for the circuit. If so, it's impossible, return -1.
# Otherwise, a solution is guaranteed to exist. Iterate through the stations, keeping track of the current tank level and a potential starting station.
# If the tank level ever drops below zero, it means the current potential start is invalid, so reset the tank and move the potential start to the next station.
# The final potential start station will be the unique solution.

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas_balance = 0
        current_tank_