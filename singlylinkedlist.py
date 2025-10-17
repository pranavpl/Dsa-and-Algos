class node:
    def __init__(self,data):
        self.data =data
        self.next = None
        pass 
    def taraverseandprint(head):
        currentnode = head
        while currentnode:
            print(currentnode.data,end="->")
            currentnode = currentnode.next
        print("null")

