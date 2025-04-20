def solve(arr):
    temp=[]
    for x in arr:
        temp.append(x)
        temp_s=sorted(temp)
        if temp_s[-1]-temp_s[0]>1:
            temp.pop()
    return len(temp)
arr=[1,1,1,2,3,3,3,2,3,2,3,2,3,2]
print(solve(arr))        
            