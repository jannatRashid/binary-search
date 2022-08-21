def binarysearch(a,n,value):
    # n=length of list
    #a=list
    #value=required data
    l=0
    r=n-1
    
    while(l<r):
        mid=(l+r)/2
        M=int(mid)
        if(value==a[M]):
          return M
        else:
            if(value<a[M]):
                r=M-1
                
            if(value>a[M]):
                l=M+1
            
    return -1




m=[2,3,4,9,11,25,35,48,55,115]
print(m)
N=10
V=int(input("enter value to be searched:"))
result= binarysearch(m,N,V)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

