class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city} - {self.zip_code}"


class Student:
    def __init__(self, name, age, address, courses=None):
        self.name = name
        self._age = None  
        self.age = age    

      
        if not isinstance(address, Address):
            raise TypeError("address must be an Address object")
        self.address = address

      
        self.courses = courses if courses is not None else []

 
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value <= 0 or value > 150:
            raise ValueError("Age must be between 1 and 150")
        self._age = value

    def add_course(self, course):
        if not isinstance(course, str):
            raise TypeError("Course must be a string")
        self.courses.append(course)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")


class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarship_amount, courses=None):
        super().__init__(name, age, address, courses)
        self.scholarship_amount = scholarship_amount

    def display(self):
        super().display()
        print(f"Scholarship: {self.scholarship_amount}")



addr = Address("GS Road", "Guwahati", "781005")

s1 = Student("Ankit", 20, addr)
s1.add_course("DSA")
s1.add_course("OS")


s2 = Student("Rahul", 21, addr, s1.courses)
s2.add_course("DBMS")

print("Student 1 Courses:", s1.courses)  
print("Student 2 Courses:", s2.courses)  

print("\n--- Student Display ---")
s1.display()

print("\n--- Scholarship Student ---")
sch = ScholarshipStudent("Priya", 22, addr, 50000)
sch.add_course("ML")
sch.display()




