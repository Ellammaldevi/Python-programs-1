class Person:  
    name = " "  
    age = 0  
  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
class Student(Person): 
    studentId = " "  
       
    def __init__(self, studentName, studentAge, studentId):  
        Person.__init__(self, studentName, studentAge) 
        self.studentId = studentId  
 
  
    def getId(self):  
        return self.studentId  
  
person1 = Person("Jefina", 23) 
person1.showName()
person1.showAge()

person2 = Person("Priya", 25)
person2.showName()
person2.showAge() 
 
student1 = Student("Ammu", 22, "102")  
student1.showName() 
student1.showAge() 
print(student1.getId()) 
 
student2 = Student("Ajay", 20, "103")
student2.showName()
student2.showAge()
print(student2.getId())  

