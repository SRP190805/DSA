def Ksum(nums,k,size=0):
    if size==0:
        size=len(nums)
    x=0
    size1=0
    for i in range(size):
        sum=0
        for j in range(i,size):
            sum+=nums[j]
            if sum==k:
                size1=j-i+1
                break
        if size1 > x:
            x=size1
    return x

def main():
    arr = [int(x) for x in input("enter the elements:").split(" ")]
    k = int(input("enter the target sum value:"))
    y = Ksum(arr,k)
    print(y)
main()