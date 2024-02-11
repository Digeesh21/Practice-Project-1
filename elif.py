a=input("Enter the Name of the student : ")
b=int(input("Enter te Roll Number of a student : "))

if (b>=0 and b<=20):
    print("Batch A")
else:
    print("Batch B")
      
c=input("Choose The Sylabus : ")    
    

if(c=="Maths"):
        print("Go to Class room No : 1 ")
elif(c=="Science"):
        print("Go to Classroom no : 2 ")
elif(c=="Arts"):
        print("Go To Class Room No : 3 ")
else:
        d=input("Enter Your Choice : ")
        
        if d=="Polytechniue":
            print("Go To Vankatram Hall")
        elif(d=="Staffs"):
            print("Then Assemble In Collage Campus")
        else:
            print("get out Of The Campus")                   
