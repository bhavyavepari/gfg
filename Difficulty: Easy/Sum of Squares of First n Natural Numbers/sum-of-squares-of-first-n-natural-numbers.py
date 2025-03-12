#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        # code here
        sum=0
        for i in range(1,number+1):
            sum+=i*i
        return sum

#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.
# Driver code
t = int(input())
ob = Solution()

for _ in range(t):
    number = int(input())
    ans = ob.sumOfSquares(number)
    print(ans)
    print("~")

# } Driver Code Ends