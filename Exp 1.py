#Problem: Two Sum 

#Problem Statement: Given an array of integers nums and an integer target, return 
#the indices of the two numbers such that they add up to target. Each input has exactly one solution, and you cannot use the same element twice.

def twoSum(nums, target):
    complement_map = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in complement_map:
            return [complement_map[complement], index]
        
        complement_map[num] = index

    return []
