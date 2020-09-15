class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        self.valores = []
        if(head != None):
            self.valores.append(head.data)
            if(head.next != None):
                head.next = self.siguienteNodo(head.next)
        return(head)

    def siguienteNodo(self, nodo):
        if(nodo.next == None):
            if(self.checkRepetido(nodo.data)):
                return(None)
            else:
                return(nodo)
        else:
            if(self.checkRepetido(nodo.data)):
                return(self.siguienteNodo(nodo.next))
            else:
                nodo.next = self.siguienteNodo(nodo.next)
                return(nodo)
                #elemento OK

    def checkRepetido(self, dato):
        lista = self.valores
        if(lista.count(dato) > 0):
            return(True)
        else:
            self.valores.append(dato)
            return(False)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
