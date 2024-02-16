class Pondicherry:
    name=""
    age=""
    def Party(self):
        print("Lets Roam in Beach")
    def Tourism(self):
        print("Lets Roam Other Places")
    
    
Digeesh=Pondicherry()
Dinesh=Pondicherry()

Digeesh.name=input("Enter the name : ")
Dinesh.name=input("Enter the name : ")

Digeesh.age=int(input("Enter the age : "))
Dinesh.age=int(input("Enter the age : "))

print(Digeesh.name)
print('age',Digeesh.age)
Digeesh.Party()

print()

print(Dinesh.name)
print('age',Dinesh.age)
Dinesh.Tourism()