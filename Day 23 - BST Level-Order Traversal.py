import sys

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

    def levelOrder(self,root):
        continuar = True
        flag_nodoraiz = True
        while(continuar):
            if not hasattr(self, 'lista_nodos'):
                self.lista_nodos = []
            if(root != None):
                if(flag_nodoraiz):
                    self.lista_nodos.append(root)
                if(root.left != None):
                    self.lista_nodos.append(root.left)
                if(root.right != None):
                    self.lista_nodos.append(root.right)
            if(len(self.lista_nodos) > 0):
                nodo_aux = self.lista_nodos[0]
                print('{}'.format(nodo_aux.data), end=' ')
                self.lista_nodos.pop(0)
                largo_lista = len(self.lista_nodos)
                if(len(self.lista_nodos) > 0):
                    root = self.lista_nodos[0]
                else:
                    continuar = False
                flag_nodoraiz = False

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
