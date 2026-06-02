# Earliest Finish Time for Land and Water Rides I
# Difficulty: Easy
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

# Brute force all combinations of one land and one water ride, considering both possible orders for each pair.
# Keep track of the minimum finish time found.

class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        overallMinFinishTime = float('inf')

        for landRideIndex in range(len(landStartTime)):
            for waterRideIndex in range(len(waterStartTime)):
                currentLandRideStart = landStartTime[landRideIndex]
                currentLandRideDuration = landDuration[landRideIndex]
                currentWaterRideStart = waterStartTime[waterRideIndex]
                currentWaterRideDuration = waterDuration[waterRideIndex]

                # Scenario 1: Land ride first, then Water ride
                landRideFinishTime = currentLandRideStart + currentLandRideDuration
                waterRideStartActual = max(currentWaterRideStart, landRideFinishTime)
                finishTimeLandFirst = waterRideStartActual + currentWaterRideDuration

                # Scenario 2: Water ride first, then Land ride
                waterRideFinishTime = currentWaterRideStart + currentWaterRideDuration
                landRideStartActual = max(currentLandRideStart, waterRideFinishTime)
                finishTimeWaterFirst = landRideStartActual + currentLandRideDuration
                
                minFinishTimeForPair = min(finishTimeLandFirst, finishTimeWaterFirst)
                overallMinFinishTime = min(overallMinFinishTime, minFinishTimeForPair)

        return overallMinFinishTime