def SecLargest(nums,size=0):
    if size == 0:
        size = len(nums)
    Largest = nums[0]
    SecLargest = -1    
    for i in range(size):
        if nums[i] > Largest:
            SecLargest = Largest
            Largest = nums[i]
        if (nums[i] > SecLargest and nums[i] != Largest):
            SecLargest = nums[i]
    print(SecLargest)        
    
arr = [int(x) for x in (input("Enter elements:").split(" "))]
SecLargest(arr)
