import random 


option=['x+','x-','y+','y-','z+','z-'] 

d= int(input("Enter the distance between the plates :"))

f=open("plotdata1.txt","w+")

def rw():
    x1=random.randint(0,30)
    y1=random.randint(0,30)
    z1=0
    
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
        
        print(x,y,z,file=f)
        
        if y==0 or y==d:
            return 
        
        
        
        x1=x
        y1=y
        z1=z
        
        
        
rw()
        
f.close()

