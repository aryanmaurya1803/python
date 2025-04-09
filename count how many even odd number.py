l1=[]
l2=[]
l3=[]
a=int(input('enter a number'))
i=0
while(i<a):
    b=int(input('enter a number you want'))
    l1.append(b)
    i+=1
for x in l1:
    if(x%2==0):
        l2.append(x)
    else:
        l3.append(x)
        
print(l1)
print('number of even number:',len(l2))
print('number of odd',len(l3))
            
        
