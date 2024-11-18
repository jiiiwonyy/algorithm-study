def DFS(L):
    if L==r:
        print(result)
    else:
        for i in range(len(nums)):
            if checklist[i]==0:
                result[L]=nums[i]
                checklist[i]=1
                DFS(L+1)
                checklist[i]=0
    

if __name__ =='__main__':
    n=int(input())
    nums=[]
    for i in range(1,n+1):
        nums.append(i)

    r=n
    result=[0]*r
    checklist=[0]*len(nums)

    DFS(0)
