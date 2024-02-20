class Solution:
    def numRabbits(self, answers: List[int]) -> int:
       '''Approach: Greedy. the problem asks to find the minimum number of
       rabbits found in a forest if we are given with a list of answers
       by asking how many rabbits are the same color as u. here we are being
       greedy on the number of rabbits in the forest. we took the assumption
       if m number of rabbits say that there are n number of rabbits the
       same color as them then n+1 rabbits are pointing to each other and
       the other have different color so we need to know how many rabbits
       have one color and then the rest will be treated the same way'''
       rabbits = 0
       rabbit_color = Counter(answers)

       '''Step2: iterate through the counter while finding the minimum number
       of rabbits who have different colors because some might be pointing
       to each other'''
       for rabbit,color in rabbit_color.items():
           number = math.ceil(color/(rabbit+1))
           rabbits = rabbits + (number * (rabbit+1))
       return rabbits
       #Time Complexity: O(n)
       #Space Complexity: O(n)