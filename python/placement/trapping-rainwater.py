# array preprocessing
def trap(height):
    if not height:
        return -1
    
    length = len(height)
    left_array = [0] * length
    right_array = [0] * length
    
    left_array[0] = height[0]
    for brick in range(1, length):
        left_array[brick] = max(left_array[brick - 1], height[brick])
    
    right_array[length - 1] = height[length - 1]
    for brick in range(length-2, -1, -1):
        right_array[brick] = max(right_array[brick + 1], height[brick])
        
    trapped_water = 0
    for brick in range(length):
        trapped_water += min(left_array[brick], right_array[brick]) - height[brick]
        
    return trapped_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap(height)
print("Trapped Water:", result)