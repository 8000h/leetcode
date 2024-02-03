def jump(nums):
    # Create varaibles to hold the max position we can reach and the end of the current jump
    max_pos, end, jumps = 0, 0, 0
    for i in range(len(nums) - 1):
        if i > end:
            return -1
        max_pos = max(max_pos, i + nums[i])
        if i == end:
            end = max_pos
            jumps += 1
    return jumps