n=int(input())

for i in range(1,n):
    if i==1:
        print(" "*(n-1)+"*")
    else:
        print(" "*(n-i)+"*"+" "*(2*(i-1)-1)+"*")

print("*"*(2*n-1))