# Count Days Spent Together
# Difficulty: Easy
# https://leetcode.com/problems/count-days-spent-together/

# Convert MM-DD dates to a day number from year start to find the intersection of two date ranges.
# Precompute cumulative days per month for efficient conversion.

class Solution:
    _days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _cumulative_days_before_month = [0] * 12
    for i in range(1, 12):
        _cumulative_days_before_month[i] = _cumulative_days_before_month[i-1] + _days_in_month[i-1]

    def _date_to_day_number(self, date_string: str) -> int:
        month = int(date_string[:2])
        day = int(date_string[3:])
        return self._cumulative_days_before_month[month - 1] + day

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_arrival_day = self._date_to_day_number(arriveAlice)
        alice_departure_day = self._date_to_day_number(leaveAlice)
        
        bob_arrival_day = self._date_to_day_number(arriveBob)
        bob_departure_day = self._date_to_day_number(leaveBob)

        overlap_start_day = max(alice_arrival_day, bob_arrival_day)
        overlap_end_day = min(alice_departure_day, bob_departure_day)

        if overlap_start_day > overlap_end_day:
            return 0
        else:
            return overlap_end_day - overlap_start_day + 1