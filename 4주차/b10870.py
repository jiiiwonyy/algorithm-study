n=int(input())

def p(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return p(n-1)+p(n-2)

print(p(n))