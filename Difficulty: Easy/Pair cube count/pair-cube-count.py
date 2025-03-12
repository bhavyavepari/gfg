#User function Template for python3
import math
class Solution:
    def pairCubeCount(self, n):
        # code here 
        count = 0
    
    
        for i in range(1, int(math.pow(n, 1/3)) + 1):
       
            cb = i * i * i
        
        
            diff = n - cb
        
        
            cbrt_diff = round(diff ** (1/3))
        
        
            if cbrt_diff * cbrt_diff * cbrt_diff == diff:
                count += 1

        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.pairCubeCount(n))
        print("~")

# } Driver Code Ends