# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        '''Approach: Union Find. The problem asks to find the lexicographically
        smallest string that is equivalent to the basestr. When we mean by equivalent
        it's going to be determined by two strings. Therefore as an intution for
        every character in the two strings at first the character itself is the
        smallest one. But when we made the equivalency between the two strings we
        simply take one of the smallest one to represent both of them since they
        are equal but since both of them might have been already represented by
        another letter we need to check are they the representative of themselves
        or not if not we need to find the representative of that. What datastructure
        would be easier to find representative of nodes? Union Find!! Therefore
        we will use union find and one edge case will be when the character
        in the given string doesn't found in both strings in that case we will
        simply use that char. Otherwise when we are finished iterating through
        both strings we will have lexicographically smallest representation of
        each character.'''

        #Step1: initially every character is the lexicographically smallest one
        parents = {}
        for s in s1:
            parents[s] = s
        for s in s2:
            parents[s] = s
        
        #to find the representative of each character
        def findParents(node):
            if node == parents[node]:
                return node
            parents[node] = findParents(parents[node])
            return parents[node]
        
        #perform union find on the given two characters
        def unionfind(u,v):
            parent_u = findParents(u)
            parent_v = findParents(v)
            #check if one of them is lexicographically smallest and substitute one by another
            if parent_u == parent_v:
                return
            if parent_u < parent_v:
                parents[parent_v] = parent_u
            else:
                parents[parent_u] = parent_v
        
        #Step2: for each equivalence call the union find if the characters are different
        for i in range(len(s1)):
            first_char = s1[i]
            second_char = s2[i]
            if first_char == second_char:
                continue
            unionfind(first_char,second_char)
        
        #Step3: build your answer by finding the parent since the parent is the lexicographically smallest one
        answer = []
        for character in baseStr:
            #check if the character exists in our dictionary
            if character not in parents:
                answer.append(character)
            else:
                parent = findParents(character)
                answer.append(parent)

        return "".join(answer)
        #Time Complexity: O(n) for performing union find inside a loop
        #Space Complexity: O(n) for holding the parent of each character