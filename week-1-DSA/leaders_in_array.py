nums=list(map(int,input().split()))
res=[]
m=float('-inf')
for r in range(len(nums)-1,-1,-1):
    if nums[r]>m:
        res.append(nums[r])
        m=nums[r]
print(res[::-1])
