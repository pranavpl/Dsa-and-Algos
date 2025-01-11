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