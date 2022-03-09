import random 

option=['x+','x-','y+','y-','z+','z-'] 

d= int(input("Enter the distance between the plates :"))
print(d)

Nmc=10000 

def rw(p0):
    x1=random.randint(0,d)
    y1=random.randint(0,d)
    z1=0
    #i=0
    while True:
        if z1==0:
            val='z+'
        else:
            val=random.choice(option)
        
        if val=='x+':
            x=x1+1
            y=y1
            z=z1
        elif val=='x-':
            x=x1-1
            y=y1
            z=z1
        elif val=='y+':
            x=x1
            y=y1+1
            z=z1
        elif val=='y-':
            x=x1
            y=y1-1
            z=z1
        elif val=='z+':
            x=x1
            y=y1
            z=z1+1
        else:
            x=x1
            y=y1
            z=z1-1
 
        if y==0 or y==d:
            return(z)
        #i+=1
        x1=x
        y1=y
        z1=z
        
  
  
 
   
list1=[]
  
f=open("rwdatad_5.txt","w+")
#f=open("rwpdata1.txt","w+")


for i in range(0,d):
        
    for j in range(0,d):
        for k in range(Nmc):
            p0=(i,j,0)
            a=rw(p0)
            #(x1,y1,z1)=d
            
            list1.append(a)
            r1_avg=sum(list1)/len(list1)
            print(r1_avg,file=f)
    
    
f.close()
	
