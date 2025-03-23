class Solution:
    def decToBinary(self, n):
        # code here
        binArr = []

        while n > 0:
            bit = n % 2
            binArr.append(str(bit))
            n //= 2

        binArr.reverse()
        return "".join(binArr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    solution = Solution()

    for _ in range(t):
        n = int(input())
        print(solution.decToBinary(n))
        print("~")

# } Driver Code Ends