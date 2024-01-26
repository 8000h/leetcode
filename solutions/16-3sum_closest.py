import sys

def three_sum_closest(nums, target):
    
    nums.sort()
    closest = sys.maxsize
    result = 0
    
    #iterating for each number in nums
    for i in range(len(nums)-2):
        left = i+1 #Index of the first number in the pair
        right = len(nums)-1 #Index of the second number in the pair
        while left < right:
            total = nums[i]+nums[left]+nums[right] #Sum of the triplet
            if abs(total-target)<closest: 
                closest = abs(total-target)
                result = total
            if total<target:
                left+=1
            elif total>target:
                right-=1
            else:
                return total #if total == target, then that's the closest possible sum to target
    return result #return the final closest sum