arr=[12,35, 1,10, 34, 5, 88, 90]
arr.sort()
n=len(arr)
a=arr[0]
c=1
for i in range(n-1):
    if a==arr[i+1]:
        c=c+1
if c==n:
    print(-1)
else:
    for j in range(n):
        if arr[n-j-1]==arr[n-j-2]:
            pass
        else:
            print(arr[n-j-2])
            break