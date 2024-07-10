def find_union(nums1, nums2):
    intersection = []
    i = 0  # Start from the beginning of nums1
    j = 0  # Start from the beginning of nums2

    while i<len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i+=1
        elif nums2[j] < nums1[i]:
            j+=1
        else:
            intersection.append(nums1[i])
            i+=1
            j+=1   
    return intersection

def main():
    arr1 = [int(x) for x in input("enter elements for first array (sorted):").split(" ")]
    arr2 = [int(x) for x in input("enter elements for second array (sorted):").split(" ")]
    result = find_union(arr1, arr2)
    print("Intersection of arrays:", result)

main()
