#User function Template for python3
from datetime import datetime
class Solution:
    def getDayOfWeek(self, d, m, y):
        # code here 
        date_obj = datetime(y, m, d)
        # Return the day of the week
        return date_obj.strftime("%A")
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        d,m,y=map(int,input().split())
        
        ob = Solution()
        print(ob.getDayOfWeek(d,m,y))
# } Driver Code Ends