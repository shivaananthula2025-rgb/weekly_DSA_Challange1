nums=list(map(int,input("Enter :").split()))
sum=nums[0]
max_sum=nums[0]
for i in range(1,len(nums)):
    sum=max(nums[i],sum+nums[i])
    max_sum=max(max_sum,sum)
print(max_sum)