#User function Template for python3


class Solution:
    def armstrongNumber (self, n):
        hundreds = n // 100
        tens = (n // 10) % 10
        ones = n % 10

    # Compute the sum of cubes
        armstrong_sum = (hundreds ** 3) + (tens ** 3) + (ones ** 3)

    # Check if Armstrong sum equals the number
        return armstrong_sum == n
#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends