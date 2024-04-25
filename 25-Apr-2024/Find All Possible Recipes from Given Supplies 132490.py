# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''Approach: Toplogical Sort. The problem asks to find out the recipes
        that could be made given the supplies and the ingredients needed. Here
        we see that there is a dependency between a recipe and it's ingredients.
        If all of the ingredients are not supplied then we can't make that
        recipe. So for each recipe we can point the ingredients it needed to
        track the dependency and increment the ingredients needed for it by
        one. This means in other words we are building a directed graph and
        starting from the ingredients which have zero in degree because they
        don't depend on anything. Therefore we start with the ingredients and
        go up when all of the ingredients are fullfiled for a recipe which
        means when it's in degree becomes zero we append it to our queue since
        it might be an ingredient for other recipes after that we check if
        the current elment is supply or recipe and add it to our answer or
        when the in degree becomes zero we can simply add it to our answer
        for space optimization.'''

        #build the graph and count the in degree for each recipe
        length = len(recipes)
        graph = defaultdict(list)
        in_degree = {recipe: 0 for recipe in recipes}
        for index in range(length):
            recipe = recipes[index]
            for ingredient in ingredients[index]:
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
            
        #perform bfs traversal on the built graph
        queue = deque()
        for supply in supplies:
            queue.append(supply)
        
        #while performing the toplogical sort add the recipes that are already made into our answer
        answer = []
        while queue:
            recipe = queue.popleft()
            for neighbour in graph[recipe]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
                    answer.append(neighbour)

        return answer
        #Time Complexity: O(V+E) where v us number of vertices and e is for edges
        #Space Complexity: O(V) for the queue