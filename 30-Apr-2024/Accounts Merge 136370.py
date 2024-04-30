# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''Approach: Union Find. The problem asks to given the emails of a
        person we need to merge accounts if they have atleast one common email.
        Therefore what we are trying to do is check if the current email already
        belongs to someone before it's just duplicate that means all the emails
        of the current index belong to the parent of that index. Therefore we are
        joining the indexes which means we need to use union find to find the
        parents and union them. After creating the link between them we simply
        need to traverse through the emails and add them to their parent index
        for that we will use a dictionary but we are adding them to their ultimate
        parent and since their parents have been joined using union find their
        ultimate parent might not be the index that they belong to in the account
        Finally we will simply add the name infront and sort the emails.'''

        #initialize rank and the parents for performing union find
        length = len(accounts)
        rank = {node:0 for node in range(length)}
        parents = {node:node for node in range(length)}

        #for finding parent of the given index perform path compression too
        def findParents(node):
            if node == parents[node]:
                return node
            parents[node] = findParents(parents[node])
            return parents[node]
        
        #perform union by rank on the given two indexes
        def unionfind(u,v):
            parent_u = findParents(u)
            parent_v = findParents(v)
            if parent_u == parent_v:
                return
            if rank[parent_u] < rank[parent_v]:
                parents[parent_u] = parent_v
            elif rank[parent_v] < rank[parent_u]:
                parents[parent_v] = parent_u
            else:
                parents[parent_u] = parent_v
                rank[parent_v] += 1
        
        '''iterate through the mails and if we have already encountered that
        mail before perform union find on the value of that and the current
        index since that mail has already been there no need to add it again
        otherwise create a link between the mail it's index.'''
        mail_node = defaultdict(int)
        for person in range(length):
            for mails in range(1,len(accounts[person])):
                mail = accounts[person][mails]
                #if the mail already exists
                if mail in mail_node:
                    unionfind(mail_node[mail],person)
                else:
                    mail_node[mail] = person
        
        #collect all mails that belong to the same parent together
        result = defaultdict(list)
        for key, value in mail_node.items():
            parent = findParents(value)
            result[parent].append(key)
        
        #build your result by adding the name infront of the mails and sorting them and appending them to our answer
        answer = []
        for key, values in result.items():
            value = [accounts[key][0]]
            value.extend(sorted(values))
            answer.append(value)

        return answer
        '''Time Complexity: O(vlogv*k + n*m) where k is number of elements in the result and
                                            v is the length of each mails at one key 
                                            n is length of the given list
                                            m is length of each mails'''
        #Space Complexity: O(n*m)
