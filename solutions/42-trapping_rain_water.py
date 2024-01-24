def trap(height):
    if not height:
        return 0

    trapped_water = 0
    max_heights_from_left = [0]*len(height)
    max_heights_from_right = [0]*len(height)

    # get max heights from left
    max_heights_from_left[0] = height[0]
    for i in range(1, len(height)):
        max_heights_from_left[i] = max(height[i], max_heights_from_left[i-1])
        
    # get max heights from right
    max_heights_from_right[-1] = height[-1]
    for i in range(len(height)-2, -1, -1):
        max_heights_from_right[i] = max(height[i], max_heights_from_right[i+1])

    # now compute the trapped water
    for i in range(len(height)):
        trapped_water += min(max_heights_from_left[i], max_heights_from_right[i]) - height[i]
        
    return trapped_water