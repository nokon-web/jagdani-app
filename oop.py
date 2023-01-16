class Student:
    def __init__(self ,id,name,department):
        self.id=id
        self.name=name
        self.department=department


student1=Student("ETS0704","Melkamu","Electrical and computer engineering")
student2=Student("ETS0811","Nardos","Electrical and computer engineering")
is_on=True
students=[student1,student2]
while is_on:
    id=input("enter your id:")
    name=input("enter your name:")
    dept=input("enter your dept:")
    student=Student(id,name,dept)
    students.append(student)
    add=input("should we continue:")
    if add=="yes":
        continue
    else:
        is_on=False


print("list of the student in the array of the student ")
print("////////////////////////////////////////////////////")
for student in students:
    print(student.id)
    print(student.name)
    print(student.department)
    print("----------------------------")
