a = 5 
print(a)
print("Hello, World!")


 recurssion 

def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0]+ list_sum(num_List[1:])
    
print(list_sum([2,3,4,5]))