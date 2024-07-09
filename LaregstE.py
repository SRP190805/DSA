def Largest(nums,size=0):
    if size == 0:
        size = len(nums)
    Largest = nums[0]    
    for i in range(size):
        if nums[i] > Largest:
            Largest = nums[i]
    print(Largest)        
    
arr = [int(x) for x in (input("Enter elements:").split(" "))]
Largest(arr)