# Problem: D - Mr. Kitayuta's Colorful Graph - https://codeforces.com/gym/540354/problem/D

class DSU:
    def __init__(self, n , m):
        self.rank = [0] * (n + 1)
        self.parent = [list(range(n + 1)) for x in range(m + 1)]
        self.size = [1] * (n + 1)
        self.count = n

    def find(self, color ,node):
        if node != self.parent[color][node]:
            self.parent[color][node] = self.find(color,self.parent[color][node])
        
        return self.parent[color][node]

def solve():
    n, m = ILT()
    ds = DSU(n+1,m+1)
    for i in range(m):
        a , b, c = ILT()
        x = ds.find(c,a)
        y = ds.find(c,b)
        ds.parent[c][x] = y

        

  
    q = I()
    for j in range(q):
        a , b = ILT()
        ans = 0
        for i in range(m+1):
            if ds.find(i,a) == ds.find(i,b):
                ans += 1
        
        print(ans)
        
   

T = 1

for _ in range(T):
    solve()