backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")
print (backpack)
def add():
    new=input("enter the no. to be added")
    backpack.append(new)
    print (backpack)
    choice=input("wants to add more ?")
    if choice == 'y':
        add()
    else:
        print (backpack)
add()