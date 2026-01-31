import json
print("WELCOME TO STUDENT MANAGMENT STUDENT\n1:Add Student\n2:View All Student\n3:View By id\n4:Update a student\n5:Delete a Student\n")

def enter_marks():
    marks={}
    subjects=["Physics","Algebra","Robotics"]
    print("Enter Marks\n")
    for index,subj in enumerate(subjects):
        while 1:
            try:
               m=int(input(f"{index+1} : {subj} = 100/"))
               if m<100 and m>0:
                  marks[subj]=m
                  break
               else:
                  print("please Enter Valid marks") 
            except ValueError:
                print("Oops : Marks Should be Integer")
    return marks

def give_id():
    while  1:
        try:
           id=int(input("Enter Student Id : "))
           return id
        except ValueError:
            print("Id must be integer\nTry Again : ")
        except Exception as e:
            print(f"Error : {e}\nTry Again : ")
            
def read_file():
    try:
      with open("data.json","r")as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        except Exception as e:
            print(f"An error occured : {e}")
    except FileNotFoundError:
        with open("data.json","w")as f:
            json.dump([],f)
        return []
    
def add_student(name,age,marks):
    students=read_file()
    
    studs={
        "id":None,
        "name":name,
        "age":age,
        "marks": marks,
        "deleted": False
    }
    students.append(studs)
    for index,l in enumerate(students,start=1):
       l["id"]=index
    with open("data.json","w")as f:
          json.dump(students,f,indent=4)
    print("Data Inserted sucessfully")

def view_all_student():
    students=read_file()
    if students:
        for obj in students:
            print(obj)
    else:
        print("Students File is Empty")
def view_by_id(id):
    students=read_file()
    for i in students:
      if i["id"]==id:
        if  i["deleted"]==True:
           print(f"Student deleted with id : {id}")
           return
        else:
            print(i)
            return
    else:
        print(f"No Student Found in File with id : {id} ")

def update_student(id,name=None,age=None,marks=None):
    students=read_file()
    for i in students:
        if i["id"]==id:
                if  i["deleted"]==True:
                   print("cant update a deleted student")
                   return
                else:
                     if name:
                         i["name"]=name
                     if age:
                         i["age"]=age
                     if marks:
                         i["marks"]=marks
    with open("data.json","w")as f:
            json.dump(students,f,indent=4)
def delete_student(id):
    students=read_file()
    for obj in students:
          if obj["id"]==id:
            students[id-1]["deleted"]=True
            print("Sucessfully Deleted")
    with open("data.json","w")as f:
         json.dump(students,f,indent=4)
    return
            

while 1:
    while 1:
      try:
         choice=int(input("Choose : "))
         break
      except ValueError:
        print("Choice should be an integer")
    match choice:
        case 1:
           
            while 1:
                while 1:
                       name=input("Enter Name : ")
                       if name.isalpha():
                           break
                       else:
                           print("Oops: Name should be String")  
                while 1:
                  try:
                    age=int(input("Enter Age : "))
                    if age is not 0:
                        break
                    else:
                        print("Oops: Age cant be 0")
                  except ValueError:
                    print("Oops : Please enter Valid Age")
                marks=enter_marks()
                break
             
            add_student(name,age,marks)
            
        case 2:
            view_all_student()
        case 3:
            id=give_id()
            view_by_id(id)
        case 4:
            id=give_id()
            students=read_file()
            for i in students:
              if i["id"]==id:
                if  i["deleted"]==True:
                   print("cant update a deleted student")
                   break
                else:
                  cho=int(input("1:Update Name\n2:Update Age\n3:Marks\n4:ALL\nChoose to update : "))
                  match cho:
                    case 1:
                        cho1=input("Enter name : ")
                        update_student(id,cho1)
                    case 2:
                        while 1 :
                            try:
                                cho2=int(input("Enter Student's Age : "))
                                break
                            except ValueError:
                                print("Oops: Age must be integer")    
                        update_student(id,None,cho2)
                    case 3:
                        marks=enter_marks()
                        update_student(id,None,None,marks)
                    case 4:
                        while 1:
                           cho1=input("Enter name : ")
                           if cho1 is not None:
                               break
                           else:
                               print("Oops : Please Enter Name")
                        while 1:
                            try:
                               cho2=input("Enter Age : ")
                               if cho2>0 and cho2 is not None:
                                   break
                               else:
                                   print("Oops : Please Enter Valid Age")
                            except ValueError:
                                print("Oops: Age must be integer")    
                        cho3=enter_marks()
                        update_student(id,cho1,cho2,cho3)
                    case _:
                       print("Choose within of parameter")
        case 5:
            id=give_id()
            delete_student(id)
        case _:
            print("Choose within of parameter")
            

