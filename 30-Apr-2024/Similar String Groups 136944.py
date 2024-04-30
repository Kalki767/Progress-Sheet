# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        '''Approach: Union Find. The problem asks to group similar words
        together. Therefore first we need to find words that have atmost
        to letters difference. At first every word is grouped with itself.
        While iterating we can find words which have atmost two letter difference
        and union them with the current word. How do we merge them using union
        find. That means we store the indexes to point to themselves at first.
        So while joining them we can update that the current index will point
        to another one so that they can become connected. We can use either
        union by rank or size to optimize the time complexity. Additionally we
        will need a hashmap to map the words with their parents so that we could
        find their ultimate parents after merging the similar ones. Finally our 
        answer will be the number of connected components we can count them
        using a set.'''
        #Step1: initialize the ultimate parent for union and parent for mapping the word with it's index
        visited = set()
        parents = {}
        ultimate_parents = {i:i for i in range(len(strs))}
        for index, word in enumerate(strs):
            parents[word] = index
        
        #Step2: define a function to find words until now that have a difference of atmost two letters
        def finddifference(word):
            answer = []
            for word2 in visited:
                counter = 0
                for index in range(len(word)):
                    if word[index] != word2[index]:
                        counter += 1
                if counter == 0 or counter == 2: #check if their difference is atmost 2
                    answer.append(word2)
            return answer
        
        #Step3: define a function to find the parents of a word
        def findParents(node):
            if node == ultimate_parents[node]:
                return node
            ultimate_parents[node] = findParents(ultimate_parents[node])
            return ultimate_parents[node]

        #Step4: define a function to union two nodes together
        def unionfind(u,v):
            parent_u = findParents(u)
            parent_v = findParents(v)
            if parent_u == parent_v:
                return
            ultimate_parents[parent_u] = parent_v
        
        #iterate through words to and update their parents while going which will group similar strings
        for word in strs:
            result = finddifference(word)
            if result:
                for val in result:
                    parent1 = parents[val]
                    parent2 = parents[word]
                    value = unionfind(parent1,parent2)
            visited.add(word)
        
        #iterate through the map find the ultimate parents of each word and add the parents
        answer = set()
        for key, value in parents.items():
            parent = findParents(value)
            answer.add(parent)

        return len(answer) #return the count of the ultimate parents
        #Time Complexity: O(n**3)
        #Space Complexity: O(n)

        