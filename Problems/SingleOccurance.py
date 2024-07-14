def SingleOccurence(nums,size=0):
    if size==0:
        size=len(nums)
    xor=0
    for i in range(size):
        xor = xor^nums[i]
    return xor

def main():
    arr = [int(x) for x in input("enter the elements:").split(" ")]
    x = SingleOccurence(arr)
    print(x)
main()