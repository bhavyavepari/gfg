#User function Template for python3
class Solution:
	def divisibleBy4 (self, N):
		# Your Code Here
		a=1
		b=0
        if int(N)%4==0:
            return a
        else:
            return b
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        s = input()
        ob = Solution()
        print(ob.divisibleBy4(s))
        print("~")

        #  Contributed By: Pranay Bansa

# } Driver Code Ends