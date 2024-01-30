def four_sum(nums, target):
    nums.sort()
    n, result = len(nums), []

    # traversing array from 0 to len - 4
    for i in range(n - 3):
        
        # not allowing same combination
        if i > 0 and nums[i] == nums[i - 1]: 
            continue
        for j in range(i + 1, n - 2): # traversing array from i + 1 to len - 3

            # not allowing same combination
            if j != i + 1 and nums[j] == nums[j - 1]: 
                continue
            l, r = j + 1, n - 1 # define two pointers
            
            # while left less than right
            while l < r: 

                # check sum equal to target
                if nums[i] + nums[j] + nums[l] + nums[r] == target: 
                    result.append([nums[i], nums[j], nums[l], nums[r]])

                    # increment left
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    l += 1

                    # decrementing right
                    while l < r and nums[r] == nums[r - 1]: 
                        r -= 1
                    r -= 1

                # when sum less than target
                elif nums[i] + nums[j] + nums[l] + nums[r] < target: 
                    l += 1

                # when sum greater than target
                else: 
                    r -= 1
    return result