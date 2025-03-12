#User function Template for python3
class Solution:
    def checkValidity(self, a: int, b: int, c: int) -> bool:
        # code here
        if(a+b>c and b+c>a and c+a>b):
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    obj = Solution()
    for _ in range(t):
        a = int(input())
        b = int(input())
        c = int(input())
        print("Valid" if obj.checkValidity(a, b, c) else "Invalid")
        print("~")

# } Driver Code Ends