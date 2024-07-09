def Zeroes(nums,size=0):
    if size==0:
        size=len(nums)      
    for i in range(size):
        if nums[i]==0:
            zero_index=i
            break
    if zero_index==-1 : return nums   
    for i in range(zero_index+1,size):
        if nums[i]!=0:
            nums[i],nums[zero_index] = nums[zero_index],nums[i]
            zero_index+=1
    return nums

def main():
   arr = [int(x) for x in input("enter elements:").split(" ")]
   x = Zeroes(arr)
   print(x)
main()