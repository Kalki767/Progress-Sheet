# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        '''Approach: Monotonic Stack. The problem asks to find out the healths of
        the remaining robots. To solve this problem let's have a basic observation.
        Two robots will collide if they are moving in different directions which
        means if the first one is moving to the right and the second one if moving
        to the left. Otherwise no collision occurs. So if a collision occurs all
        we have to do is follow the rules to determine whether to destroy both of
        them or just one of them and decrement the health by one.'''
        # Create a list to store positions, healths, and indices together
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(len(positions))])
        
        stack = []  # To keep track of robots moving right
        result = [None] * len(positions)  # To store the final healths of robots
        
        # Go through each robot based on sorted positions
        for pos, health, direction, index in robots:
            # If moving right, push to the stack
            if direction == 'R':
                stack.append((health, index))
            else:
                # Robot is moving left, check for collisions with robots in the stack
                while stack and health > 0:
                    # Pop the last robot moving to the right
                    right_health, right_index = stack[-1]
                    
                    # If they have the same health, both are destroyed
                    if right_health == health:
                        stack.pop()  # Remove the robot from the stack
                        health = 0   # This robot also gets destroyed
                    elif right_health > health:
                        # The right-moving robot survives with reduced health
                        stack[-1] = (right_health - 1, right_index)
                        health = 0  # This robot is destroyed
                    else:
                        # The left-moving robot survives, destroy the right-moving robot
                        stack.pop()  # Remove the robot from the stack
                        health -= 1  # Left-moving robot loses 1 health
        
            # If the left-moving robot survives after collision, add to result
            if health > 0 and direction == 'L':
                result[index] = health
        
        # Now, add all the remaining right-moving robots to the result
        for right_health, right_index in stack:
            result[right_index] = right_health
        
        # Filter out None values, which represent robots that were destroyed
        return [r for r in result if r is not None]
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n) where n is the total number of robots