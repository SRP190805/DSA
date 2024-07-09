def Duplicates(nums,x,size=0):
    if size==0:
        size = len(nums)
    i=0
    for j in range(size):
        a = nums[j]
        x[a]+=1
        #if nums[i]!=nums[j]:
        #    i+=1
        #    nums[i]=nums[j]
    for j in range(len(x)):
        if x[j]!=0:
            i+=1
    return (i+1)        

def main():
    arr = [int(x) for x in (input("Enter elements:").split(" "))]
    hash = [0] * (max(arr) +1)
    a = Duplicates(arr,hash)
    res = [x for x in range(max(arr)+1) if hash[x]!=0]
    print(res)
    print(arr)
main()