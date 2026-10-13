with open ("aps.txt","w")as f:
   f.write("Hyy Im Arpit Singh Patel\n")


with open ("aps.txt","r") as f:

     line1= f.readline()
     line2= f.readline()
     print(line1)
     print(line2)


with open ("aps.txt","a") as f:
    f.write("last line\n")     
