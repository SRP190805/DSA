def Duplicates(nums,x,size=0):
    if size==0:
        size = len(nums)
    i=0
    for j in range(size):
        a = nums[j]
        x[a]+=1
    return ()        

def main():
    arr = [int(x) for x in (input("Enter elements:").split(" "))]
    hash = [0] * (max(arr) +1)
    Duplicates(arr,hash)
    res = [x for x in range(max(arr)+1) if hash[x]!=0]
    print(res)
main()
