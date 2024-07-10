def find_union(nums1, nums2):
    union = []
    i = 0  # Start from the beginning of nums1
    j = 0  # Start from the beginning of nums2

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            # Add element from nums1 if it's not already in the union
            if nums1[i] not in union:
                union.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            # Add element from nums2 if it's not already in the union
            if nums2[j] not in union:
                union.append(nums2[j])
            j += 1
        else:  # nums1[i] == nums2[j] (common element)
            # Add the common element only once
            if nums1[i] not in union:
                union.append(nums1[i])
            i += 1
            j += 1

    # Add remaining elements from either array (if not already added)
    while i < len(nums1):
        if nums1[i] not in union:
            union.append(nums1[i])
        i += 1

    while j < len(nums2):
        if nums2[j] not in union:
            union.append(nums2[j])
        j += 1

    return union

def main():
    arr1 = [int(x) for x in input("enter elements for first array (sorted):").split(" ")]
    arr2 = [int(x) for x in input("enter elements for second array (sorted):").split(" ")]
    result = find_union(arr1, arr2)
    print("Union of arrays:", result)

main()
