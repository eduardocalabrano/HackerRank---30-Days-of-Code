class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        self.nivel_actual(root) #Se actualiza el nivel del nodo al entrar
        if(root.left != None):
            self.getHeight(root.left)
            self.nivel_actual(root) #Se actualiza el nivel del nodo post revision de nodos izquierdos
        if(root.right != None):
            self.getHeight(root.right)
            self.nivel_actual(root)#se actualiza el nivel del nodo post revision de nodos derechos
        return(self.maximo)


    def nivel_actual(self, root):
        if hasattr(self, 'nivel'):
            if hasattr(root, 'floor'):
                self.nivel -= 1
            else:
                self.nivel += 1
                root.floor = self.nivel
                if(self.nivel > self.maximo):
                    self.maximo = self.nivel
        else:
            self.nivel = 0
            root.floor = 0
            self.maximo = 0
        #print('Nos encontramos en el piso {}'.format(self.nivel))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
