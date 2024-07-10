def MaxConse1(nums,size=0):
    if size==0:
        size=len(nums)
    max=0
    cnt=0
    for i in range(size):
        if nums[i]==1:
            cnt+=1
        else:
            if cnt>max:
                max=cnt
                cnt=0
    return max

def main():
    arr =[int(x) for x in input("enter the elements:").split(" ")]
    x = MaxConse1(arr)
    print(x)
main()