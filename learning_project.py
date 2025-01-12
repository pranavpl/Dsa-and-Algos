#data types & oprations
def basic_operations():
    #num and basic math 
    x=5
    y=5
    print(f"Basic math:")
    print(f"add: { x + y }")
    print(f"sub: {x-y}")
    print(f"mul:{x*y}")
    print(f"Division:{x/y}")
    print(f"Integer Division:{x//y}")
    print(f"Modulus:{x%y}")
    print(f"Power{x**y}")

#strings

name = "Python"
print(f"\nString operations:")
print(f"Orginal String {name}")
print(f"Uppercase{name.upper()}")
print(f"Length: {len(name)}")
print(f"Replac:{name.replace('n','N')}")
print(f"Slice: {name[1:4]}")


# Lists and List Comprehension


def list_opre():
    # Basic list operations
    number = [ 1,2,3,4,5]
    fruits = ['apple','banana','orange']

    print(f"List Operations:")
    print(f"Orginal list:{number}")
    number.append(6)
    print(f"After append{number}")
    number.insert(0,0)
    print(f"After insert:{number}")
    number.remove(3)
    print(f"After reove:{number}")

# List comprehension

sqr = [x**2 for x in range(5)]
evennum = [x for x in range(10)if x % 2 == 0]
print(f"\nList Comprehension:")
print(f"Squares:{sqr}")
print(f"Even number:{evennum}")


# Dictionaries and Sets

def dictandset ():
    student ={
        'name':'John',
        'age': 20 ,
        'grades': [ 56,45,63 ]
    }

    print(f"Orginal dict{student}")
    student['city'] = 'NYC'
    print(f"After Adding key:{student}")
    print(f"keys: {student.keys()}")
    print(f"values:{student.values()}")

# Set operations
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(f"\nSet Operations:")
print(f"Union: {set1.union(set2)}")
print(f"Intersection:{set1.intersection(set2)}")
print(f"Difference:{set1.difference(set2)}")


# Functions and Lambda
def demonstrate_function():
    # Regular function
    def calculated_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'F'
        
    square = lambda x:x**2
    print(f"Functions:")
    print(f"Grade for 85:{calculated_grade(85)}")
    print(f"Square of 5:{square(5)}")

# Object-Oriented Programming
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grd(self,grade):
        self.grades.append(grade)

    def getavg(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0
    
    def __str__(self):
        return f"Student(name={self.name},age{self.age},average={self.getavg():.2f})"


#Error handling

def error_handling_example():
    try:
        result = 10/0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        print("This will always execute")
        

# File Operations
def file_operations():
    #writting to file 
    with open('example.txt','r') as f:
        content=f.read()
        print(f"File content: {content}")


