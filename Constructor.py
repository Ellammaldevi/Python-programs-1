class Employee:
      
    def __init__(self,name,id,age):  
        self.id = id;  
        self.name = name; 
        self.age = age; 
        
    def display (self):  
        
        print("ID: %d \nName: %s \nAge: %d"%(self.id,self.name,self.age)) 
         
emp1 = Employee("Hari", 101, 25)  
emp2 = Employee("Jegan", 102, 30)  
emp3 = Employee("Kumar", 103, 35)
  
   
emp1.display();   
emp2.display(); 
emp3.display();  
