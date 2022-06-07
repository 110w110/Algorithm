global count
count = 0
def z(x,y,n,r,c):
    global count
    global isDone
    if n==1:
        if x==c and y==r:
            print(count)
        count += 1
        if x+1==c and y==r:
            print(count)
        count += 1
        if x==c and y+1==r:
            print(count)
        count += 1
        if x+1==c and y+1==r:
            print(count)
        count += 1
        return
    if c>=x and c<x+2**(n-1) and r>=y and r<y+2**(n-1):
        z(x, y, n - 1, r, c)
    count += 4**(n-1)
    if c>=x+2**(n-1) and c<x+2**n and r>=y and r<y+2**(n-1):
        z(x+2**(n-1),y,n-1,r,c)
    count += 4**(n-1)
    if c>=x and c<x+2**(n-1) and r>=y+2**(n-1) and r<y+2**n:
        z(x,y+2**(n-1),n-1,r,c)
    count += 4**(n-1)
    if c>=x+2**(n-1) and c<x+2**n and r>=y+2**(n-1) and r<y+2**n:
        z(x+2**(n-1),y+2**(n-1),n-1,r,c)
    count += 4**(n-1)
    return

n, r, c = map(int,input().split())
z(0,0,n,r,c)
