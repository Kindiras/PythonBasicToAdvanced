a = "HiEveryBody"

if((n:=len(a))>5):
    print(f'The value is too large {n}')

while((n:=len(a))>1):
    print(n)
    a=a[:-1]    