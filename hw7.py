class Node:
    def __init__(self,data,ID):
        self.parent = None
        self.left = None
        self.right = None
        self.ID = ID
        self.data = data

    def insertLeft(self,data,ID,parent):
        if self.left is None:
            self.left = Node(data,ID)
            self.left.parent = parent
    def insertRight(self, data, ID,parent):
        if self.right is None:
            self.right = Node(data,ID)
            self.right.parent = parent
            
    def add(self,p,g, user1, a ,user2,b , key):
    #solve for new k value
        #solve for k
        K = pow(g,a*b)
        K = K % p
        #find sponsor
        sponsor = self.findUser(user1)
        # #replace sponsor wit k0
        sponsor.ID = key
        sponsor.data = K
        
        #insert new user1 
        sponsor.insertLeft(a, user1, sponsor)

        #insert user2
        sponsor.insertRight(b,user2, sponsor)
        
        sponsor.parent.reCalculate(p,g)
    
    def reCalculate(self,p,g):
        if self is not None:
            #retrive data of left and right
            a = self.left.data
            b = self.right.data
            #solve K
            K = pow(g,a*b)
            K = K % p
            
            self.data = K
            if self.parent is not None:
                self.parent.reCalculate(p,g)
            
        
         
    def findUser(self, ID):
        if self == None:
            return None
        if self.left is None and self.right is None:
            if self.ID == ID:
                return None
            else:
                return self
        key_node = None
        q = []
        q.append(self) 
        temp = None
        
        while(len(q)):
            temp = q.pop(0)
            if temp.ID == ID:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right) 
        
        return key_node
                    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.ID,self.data)
        if self.right:
            self.right.printTree()

def init(p,g, user1, a ,user2,b , key):
#solve for k0 value
    #solve for k
    K = pow(g,a*b)
    K = K % p
    #make new root node and return
    root = Node(K,key)
    #add alice and bob to left and right node
    root.insertLeft(a, user1,root)
    root.insertRight(b, user2,root)
    
    return root

root = init(29,3,"Alice",7, "Bob", 5, "K0")
root.add(29,3,"Alice",3,"Carol",13,"K1")
root.add(29,3,"Carol",6,"David",20,"K2")
root.add(29,3,"Carol",2,"Earl",17,"K3")
print("root",root.ID)
root.printTree()
