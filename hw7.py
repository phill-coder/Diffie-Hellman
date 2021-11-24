class Node:
    def __init__(self,data,ID):
        self.left = None
        self.right = None
        self.ID = ID
        self.data = data

    def insert(self,data,ID):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data,ID)
                else:
                    self.left.insert(data,ID)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data,ID)
                else:
                    self.right.insert(data,ID)
        else:
            self.ID = ID
            self.data = data
    
    def add():
        #solve for new k0 value
        print("hello")
        #find alice

        #replace alice wit k0

        #insert new alice 

        #insert carol
    
    def findUser(self, ID):
    
        if self.right:
            if(self.right.ID == ID):
                print("found",self.right.ID)
                return self.right.ID
            else:
                self.right.findUser(ID)  
        if self.left:
            if(self.left.ID == ID):
                print("found",self.left.ID)
                return self.left.ID
            else:
                self.left.findUser(ID)
        else:
            return self
        



    def test(self, ID):
        print(self.findUser(ID))
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = Node(12, "ryan")
root.insert(5, "josh")
root.insert(2, "tan")
root.insert(9, "phil")
root.insert(23, "dil")

root.printTree()
root.test("tan")

