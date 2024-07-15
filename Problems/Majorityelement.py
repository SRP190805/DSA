def MajorityEl(arr,n):
    cnt=0
    el=0
    for i in range(n):
        if cnt==0:
            cnt=1
            el=arr[i]
        elif arr[i]==el:
            cnt+=1
        else:
            cnt-=1
    cnt1=0
    for i in range(n):
        if arr[i]==el:
            cnt1+=1
    if cnt1>(n//2):
        return el
    return -1

def main():
    arr = [int(x) for x in input("enter the elements:\n").split(" ")]
    x = MajorityEl(arr,len(arr))
    print(x)
main()