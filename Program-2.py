def integer(a):
    i=1
    j=0
    items=[]
    while(j<a):
        if(i%2!=0):
            j=j+1
            items.append(i)
        i=i+1
    print(items)
a=int(input())
integer(a)
