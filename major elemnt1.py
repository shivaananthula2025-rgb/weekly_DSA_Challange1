nums=list(map(int,input("Enter :").split()))
n=len(nums)
seen={}
c=0
for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
for j in seen:
    if seen[j]>n//2:
        print(j)

'''
Time Complexity: O(n)
space Complexity: O(n)
'''