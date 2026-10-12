def arp():
    a=5 
    print ("Value of a:" , a)

arp()  


def avg(a=3,b=4):
    avgvalue = (a+b)/2
    print ("Average value is:" , avgvalue)

avg(2,7)
avg(2,5)
avg(2,1)
avg()

def show_age(name ,age):
    print(f"my name is {name} and I am {age} years old")

show_age("Arpit", 19)   

def multiply(a,b):
    return a*b
print (multiply(2,3))
result = multiply(5,6)
print (result)