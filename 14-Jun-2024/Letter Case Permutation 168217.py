# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''Approach: Backtracking. The problem asks to find all permutation
        of the given string by changing capitals to smalls and smalls to 
        capitals. So all we have to do is check if the current character is
        digit or letter. If it's a letter we don't have to do anything but
        if it's a letter we will obviously have two cases either to take it as
        it is or to change it's case either into upper or lower. Finally when
        we reach the end we will simply concatenate the resulting string and
        add it to our list. We used a list instead of a string because string 
        concatenation takes more time than list append. But inorder to remove
        the space complexity issued by the call stack we used bitmasks whether
        we have used the current character or not if we have then we will take
        it's opposite case if not we will take itself since this might end up
        in giving as duplicate values we will use set to avoid duplication.'''
        ans = set()
        n = len(s)
        
        # There are 2^len(s) possible permutations
        for mask in range(2 ** n):
            t = list(s) #Since strings are immutable convert it to list
            for i in range(n):
                if s[i].isalpha():  # Only toggle case for alphabetic characters
                    if mask & (1 << i):
                        t[i] = t[i].upper() if t[i].islower() else t[i].lower()
                    
            ans.add("".join(t))
        
        return list(ans)

        #Time Complexity: O(2**n * n)
        #Space Complexity: O(2**n)

        '''Backtracking Solution:
        result = []
        def backtrack(index,current):
            if index == len(s):
                result.append("".join(current))
                return 
            if s[index].isdigit():
                current.append(s[index])
                backtrack(index+1,current)
            else:
                letter = s[index]
                if letter.islower():
                    current.append(letter)
                    backtrack(index+1,current)
                    current.pop()
                    current.append(letter.upper())
                    backtrack(index+1,current)
                else:
                    current.append(letter)
                    backtrack(index+1,current)
                    current.pop()
                    current.append(letter.lower())
                    backtrack(index+1,current)
            current.pop()
            return
        backtrack(0,[])
        return result
        '''
