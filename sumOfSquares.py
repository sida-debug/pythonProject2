def sum_quares(nums):
   sum = 0
   for i in range(len(nums)):
      sum+=pow(nums[i],2)
   return sum

print(sum_quares([1,2,4,5]))