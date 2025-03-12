#User function Template for python3

class Solution:
    def isPerfectNumber(self, n):
        # code here 
        if n <= 1:
            return False

        sum_divisors = 1  # 1 is always a divisor
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_divisors += i
                if i != n // i:  # Add the corresponding divisor if it's different
                    sum_divisors += n // i

        return sum_divisors == n

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ans = (ob.isPerfectNumber(N))
        if (ans):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends