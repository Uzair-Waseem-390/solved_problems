# Sum Game
# Difficulty: Medium
# https://leetcode.com/problems/sum-game/

# The game outcome depends on the initial difference in sums and the difference in question mark counts.
# If the number of question marks on each side is equal, Alice can always counter Bob's optimal move,
# so the game outcome is determined by the initial sum difference.
# If the number of question marks is unequal, the player with more question marks on their preferred side
# (e.g., Alice on left, Bob on right) can force a specific outcome related to the difference in question marks,
# but only if the remaining '?' counts are also unequal.
# Ultimately, it boils down to the final difference in sum of digits and the final difference in question mark counts.
# The parity of total question marks determines whose turn it is for the last question mark.