# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Examples:

# Input: arr[] = [1, 4, 3, 2, 6, 5]  
# Output:  [5, 6, 2, 3, 4, 1]
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = [4, 5, 1, 2]
# Output: [2, 1, 5, 4]
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.


def reverseArray(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

# print(reverseArray([1, 4, 3, 2, 6, 5]))


# ------------------------------------------------------------------------------------------------------------------------------

# Given an array of integers arr[], the task is to find the maximum and minimum elements in the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = [3, 5, 4, 1, 9]
# Output: [1, 9]
# Explanation: The minimum element is 1, and the maximum element is 9.

# Input: arr[] = [22, 14, 8, 17, 35, 3]
# Output: [3, 35] 
# Explanation: The minimum element is 3, and the maximum element is 35.


# Brute force 

def minAndMax(arr):
    n=len(arr)
    mini=arr[0]
    maxi=arr[0]
    for i in range(n):
        if arr[i]<mini:
            mini=arr[i]
        if arr[i]>maxi:
            maxi=arr[i]
    return [mini,maxi]


# print(minAndMax([3, 5, 4, 1, 9]))

# -------------------------------------------------------------------------------------------------------------

# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

# Note: The kth smallest element is determined based on the sorted order of the array.

# Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
# Output: 5
# Explanation: 4th smallest element in the given array is 5.
# Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: 3rd smallest element in the given array is 7.

def kthMinAndMax(arr,k):
    #  on hold need to learn sorting techniques actually 
    pass
# print(kthMinAndMax([10, 5, 4, 3, 48, 6, 2, 33, 53, 10],4))

