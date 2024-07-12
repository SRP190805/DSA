#Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.
#In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

def subArraySum(arr, n, s): 
       #Write your code here
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=arr[j]
                if sum==s:
                    break
            if sum==s:
                return (i+1,j+1)
        return -1
   
def main():
    arr = [int(x) for x in input("enter the elements:").split(" ")]
    k = int(input("enter the target sum value:"))
    x = len(arr)
    y = subArraySum(arr,x,k)
    print(y)
main()