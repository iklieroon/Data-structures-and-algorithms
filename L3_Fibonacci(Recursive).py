#F(0)=0, F(1)=1, f(n)=F(n-1)+F(n-2) for n>=2
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        # This is a recursive function as fibonacci is called in itself
    
print(fibonacci(12))