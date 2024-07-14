def Leader(arr, n):
    leaders = []

    # The rightmost element is always a leader
    leaders.append(arr[n - 1])

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= leaders[-1]:
            leaders.append(arr[i])

    return leaders[::-1]  # Reverse the leaders list

def main():
    arr = [int(x) for x in input("enter the elements of array:\n").split(" ")]
    leaders = Leader(arr, len(arr))
    print(leaders)

main()
