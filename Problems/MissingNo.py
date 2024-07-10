def MissingNo(nums,d,size=0):
    n = d-1
    xor1=0
    xor2=0
    for i in range(n):
        xor2 = xor2^nums[i]
        xor1 = xor1^(i+1)
    xor1 =xor1^d
    return (xor1^xor2)
        

def main():
    arr =[int(x) for x in input("enter the elements:").split(" ")]
    d = int(input("enter the actual range of array:"))
    x = MissingNo(arr,d)
    print(x)
main()
    