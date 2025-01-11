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

dictandset()
