#Input two numbers n1 and n2
n1 = int(input("Enter the 1st number?"))
n2 = int(input("Enter the 1st number?"))
gcd = 1
#SPECIAL CASES Best case: O(1)
#CASE 1: Both n1 and n2 are zero
if(n1 == 0 and n2 == 0):
    gcd = 0
#if either n1 or n2 is zero or both are equal
elif(n1 == 0 or n2 == 0 or n1 == n2):
    if(n1 >= n2):
        gcd = n1
    else:
        gcd = n2
#if both n1 and n2 are 1
elif(n1 == 1 or n2 == 1):
    if(n1 == 1):
        gcd = n2
    else:
        gcd = n1
#Still worst case : O(n)
else:
    if(n1<n2):    #choose the smallest number between n1 and n2
        n = n1
    else:
        n = n2
        """Instead of starting at 2 where we will always have to check all the numbers
        from 2-n we can start at n and go down to 2"""
    for i in range(n,1,-1):
        if(n1 % i == 0 and n2 % i == 0):
            gcd = i
            break

print("Greatest Common Division Using Brute Force is: ",gcd)
