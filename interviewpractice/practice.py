"""
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9



def two_sum(nums, target):
    # Step 1: Initialize an empty dictionary to store indices of numbers
    index_map = {}
    
    # Step 2: Loop through the list of numbers
    for i, num in enumerate(nums):
        # Step 3: Calculate the complement needed to reach the target
        complement = target - num
        
        # Step 4: Check if the complement exists in the dictionary
        if complement in index_map:
            # If it exists, return the pair of indices
            return [index_map[complement], i]
        
        # Step 5: If not, add the current number and its index to the dictionary
        index_map[num] = i


"""


def two_sum(nums, target):
    # Step 1: Initialize an empty dictionary to store indices of numbers
    index_map = {}
    
    # Step 2: Loop through the list of numbers
    for i, num in enumerate(nums):
        # Step 3: Calculate the complement needed to reach the target
        complement = target - num
        
        # Step 4: Check if the complement exists in the dictionary
        if complement in index_map:
            # If it exists, return the pair of indices
            return [index_map[complement], i]
        
        # Step 5: If not, add the current number and its index to the dictionary
        index_map[num] = i



nums=[ 2,7,11,15]
target = 18

print (two_sum(nums,target))
            
