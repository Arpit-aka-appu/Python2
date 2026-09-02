#write a program that takes input as a favourite food and prints it
food1 = input("favorite food is :")
food2 = input("favorite food is :")
fc = food1[1:5], food2[1:5]
fd = food1[4:], food2[4:]
print ("The middle 3 letters are :",fc )
print ("the last 2 letters are : ",fd)