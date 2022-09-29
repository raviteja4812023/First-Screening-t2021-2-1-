def CountFrequency(my_list):
    freq={}
    i=1
    while(i<=9):
        count=0 
        for j in my_list:
            if(j%i==0):
                count+=1
        freq[i]=count
        i=i+1
    for key,value in freq.items():
        print("%d: %d"%(key,value))
 
my_list =[1,2,8,9,12,46,76,82,15,20,30]
CountFrequency(my_list)
