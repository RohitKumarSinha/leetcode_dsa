def LongestSubsetWithZeroSum(arr):

    # Dictionary to store the cumulative sum up to all indices
    hash_map = {}
    
    max_length = 0  # Initialize the maximum length of subarray
    current_sum = 0  # Initialize sum of elements
    
    for i in range(len(arr)):
        current_sum += arr[i]  # Add the current element to the cumulative sum
        
        if arr[i] == 0 and max_length == 0:
            max_length = 1
        
        if current_sum == 0:
            max_length = i + 1
        
        # Check if this sum is seen before
        if current_sum in hash_map:
            # If yes, update max_length if required
            max_length = max(max_length, i - hash_map[current_sum])
        else:
            # Else, add this sum with index to the hash_map
            hash_map[current_sum] = i
            
    return max_length