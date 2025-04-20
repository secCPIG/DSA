p=int(input())
for i in range(p):
    a=list(input().split())
    ai = []
    for s in a:
        ai.append(int(s))
    c1=ai[0]+ai[1]
    c2=ai[2]-ai[1]
    c3=ai[3]-ai[2]
    f=1
    if c1==c2==c3:
        print(3)    
    elif c1==c2 or c2==c3 or c3==c1:
        f=f+1
        print(f)
    else:
        print(1)    


   




