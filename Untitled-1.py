pizza=input("do you want a pizza?(y/n)")
size=input("select size of a pizza \nsmall pizza(s)=100Rs"
           "y\nmedium pizza(m)=200Rs\nlarge pizza(l)=300Rs")
if size=="s"or size=="S":
    bill=100
elif size=="m"or size=="M":
    bill=200
else:
    bill=300
pepperoni = input("do you want pepperoni?(y/n)")
if pepperoni == "y" or pepperoni == "Y":
    if size=="s"or size=="S":
        bill = bill + 30
    else:
        bill=bill+50
cheese=input("do you want extra cheese?(y/n)")
if cheese=="y"or cheese=="Y":
    bill=bill+20
print(f"your bill is {bill}.")