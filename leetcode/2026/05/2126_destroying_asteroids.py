# Destroying Asteroids
# Difficulty: Medium
# https://leetcode.com/problems/destroying-asteroids/

# Greedy approach: sort asteroids by mass and process them in ascending order. This maximizes planet mass to overcome larger asteroids later.
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        current_planet_mass = mass
        
        asteroids.sort()
        
        for asteroid_mass in asteroids:
            if current_planet_mass >= asteroid_mass:
                current_planet_mass += asteroid_mass
            else:
                return False
                
        return True