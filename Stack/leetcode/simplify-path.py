class Solution:
    def simplifyPath(self, path: str) -> str:
        '''Approach: Stack. the problem asks to return a directory after
        making changes to it. if we have a .. then we go back if there
        is something to go back. if we have a . we stayed where we are
        we then finally return what remains in the stack'''
        
        #split the string in to lists using the slash
        Paths = path.split('/')
        Paths = [paths for paths in Paths if paths != "" ]
        #use stack to store the current directory
        stack = []
        for paths in Paths:
            '''if the stack is empty there is nowhere to return to or stay
            so continue otherwise append the directory name'''
            if not stack:
                if paths == '..' or paths == '.':
                    continue
                else:
                    stack.append(paths)
            else:
                if paths == '..':
                    stack.pop()
                elif paths == '.':
                    continue
                else:
                    stack.append(paths)
        canonical_path = '/' + "/".join(stack)
        return canonical_path
        #Time Complexity: O(n)
        #Space Complexity: O(n)