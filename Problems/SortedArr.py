def IsSorted(nums,size=0):
    if size == 0:
        size = len(nums)  
    for i in range(1,size):
        if nums[i] >= nums[i-1]:
            pass
        else:
            return False
    return True
    
arr = [int(x) for x in (input("Enter elements:").split(" "))]
print(IsSorted(arr))
