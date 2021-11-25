import sys

out = sys.stdout
class Node:
    def __init__(self,data,ID):
        self.parent = None
        self.left = None
        self.right = None
        self.ID = ID
        self.data = data

    def insertLeft(self,data,ID,parent):
        if self.left == None:
            self.left = Node(data,ID)
            self.left.parent = parent
    def insertRight(self, data, ID,parent):
        if self.right == None:
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
    
    def delete(self,p,g,user,a):
        #find user to delete
        delUser = self.findUser(user)

        #goto parent 
        parent = delUser.parent

        #check if lef or right is to be delted
        if parent.left.ID == user:
            newNode = parent.right
        else:
            newNode = parent.left
        
        #delete user
        delUser = None
        
        if newNode.left == None and newNode.right == None:
            #replace parent info wit newNode and delete it
            
            parent.ID = newNode.ID
            parent.data = a
            parent.left = None
            parent.right = None
            newNode = None

        else:
            #replace k below with k ontop
            #save original parent to set left
            OGparent = parent
            #save parent to use to set new parent
            temp = parent.parent 
            #replace parent wit other node
            parent = newNode
            #set parent node with orginal parent parent's
            parent.parent = temp
            #the grandparent node left\right is the old node so set it as the new node
            if parent.parent.left.ID == OGparent.ID:
                parent.parent.left = parent
            else:
                parent.parent.right = parent
            newNode = None
            
        
        #recalculate nodes
        parent.parent.reCalculate(p,g)
                   
    def reCalculate(self,p,g):
        if self != None:
            #retrive data of left and right
            a = self.left.data
            b = self.right.data
            #solve K
            K = pow(g,a*b)
            K = K % p
            
            self.data = K
            if self.parent != None:
                self.parent.reCalculate(p,g)
    
    def query(self, keyID):
        if self.left:
            self.left.query(keyID)
        if self:
            if self.ID == keyID:
                out.write(str(self.data)+'\n')
        if self.right:
            self.right.query(keyID)
        
        
         
    def findUser(self, ID):
        if self == None:
            return None
        if self.left == None and self.right == None:
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
inputAmt = 0
p = 0
q = 0
actions = 0
root = None
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    line = line.strip('\n')
    if inputAmt == 0:
        #set p and q
        PQ = line.split(' ')
        p = int(PQ[0])
        q = int(PQ[1])
    if inputAmt == 1:
        #set action amt
        actions = int(line)
    if inputAmt == 2:
        #initalize root
        info = line.split(' ')
        root = init(p,q,info[0],int(info[1]),info[2],int(info[3]),info[4])
    if "QUERY" in line:
        key = line.split(' ')
        root.query(key[1])
    if "ADD" in line:
        info = line.split(' ')
        root.add(p,q,info[1],int(info[2]), info[3],int(info[4]),info[5])
    if "DEL" in line:
        info = line.split(' ')
        root.delete(p,q,info[1],int(info[2]))
    
    #track line
    inputAmt = inputAmt + 1