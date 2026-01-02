def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Sliding Window Problem
        
        if sum(nums) < target:
            return 0
        
        if sum(nums) == target:
            return len(nums)

        n = len(nums)
        left = 0 
        current_sum = 0
        minLen = float('inf')

        for right in range(n):
             current_sum += nums[right]

             while (current_sum >= target):
                  minLen = min(minLen, right - left + 1)
                  current_sum -= nums[left]
                  left += 1
            
        return minLen

print(minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))