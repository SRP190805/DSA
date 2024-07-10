def Lrotate(nums,d,size=0):
    if size==0:
        size=len(nums)
    d=d%size
    left=nums[:d]
    right=nums[d:]
    right.extend(left)
    return right

def Rrotate(nums,d,size=0):
    if size==0:
        size=len(nums)
    d=size-(d%size)
    left=nums[:d]
    right=nums[d:]
    right.extend(left)
    return right

def main():
    arr = [int(x) for x in input("enter the elements:").split(" ")]
    d = int(input("enter the number of rotations:"))
    x = Lrotate(arr,d)
    y = Rrotate(arr,d)
    print(x,y)

main()