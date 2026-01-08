class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"\nPerson name: {self.name}" )
        print(f"Person age = {self.age}\n")
    
class Student(Person):
    def __init__(self,name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f"\nStudent name: {self.name}" )
        print(f"Student age = {self.age}")
        print(f"Student section: {self.section}\n")

person1 = Person("Georgi Georgiev", 37)
student1 = Student("Ivan Ivanov", 23, "Networking")

person1.display()
student1.displayStudent()