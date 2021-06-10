class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LL:
    def __init__(self):
        self.head=None
    def insertend(self,data):
        itr=self.head
        while itr:
            if(itr.next==None):
                break
            itr=itr.next
        itr.next=Node(data,None)

    def reverse(self):
        if(self.head==None):
            return
        if(self.head.next==None):
            return
        else:
            a = self.head
            itr = a.next
            a.next = None
            while (itr):
                b = itr.next
                itr.next = a
                a = itr
                itr = b
            self.head = a

    def dele(self,pos):
        itr=self.head
        for i in range(pos-2):
            itr=itr.next
        itr.next = (itr.next).next

    def specificpos(self,data,pos):
        itr=self.head
        for i in range(pos-2):
            itr=itr.next
        nn=Node(data,itr.next)
        itr.next=nn

    def insertbig(self,data):
        node=Node(data,self.head)
        self.head=node
    def pri(self):
        if self.head==None:
            print("empty LL")
            return

        itr=self.head
        llstr=""

        while itr:
            llstr+=str(itr.data) + "->"
            itr=itr.next
        print(llstr)

    def delbyvalue(self,d):
        itr=self.head
        if(itr.data==d):
            self.head=itr.next
            return
        while itr:
            if((itr.next).next==None):
                if((itr.next).data==d):
                    itr.next=None
                    return
                else:
                    print("there is not a value like this")
                    return

            if((itr.next).data==d):
                itr.next=(itr.next).next
                return
            itr=itr.next

# ll=LL()
# ll.insertbig(10)
# ll.insertbig(9)
# ll.insertbig(8)
# ll.insertend(11)
# ll.insertend(12)
# ll.specificpos(9.5,3)
# #ll.dele(3)
# #ll.delbyvalue()
# ll.pri()
#******************************************************************************************************************
#******************************************************************************************************************
##******************************************************************************************************************
#******************************************************************************************************************
##******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
#******************************************************************************************************************
##******************************************************************************************************************
#******************************************************************************************************************

class dnode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None

    def insertatstart(self,d):
        nn=dnode(d)
        if self.head==None:
            nn.prev=nn.next=None
            self.head=nn
        else:
            itr=self.head
            nn.next=itr
            nn.prev=None
            itr.prev=nn
            self.head=nn

    def insertatend(self,d):
        if self.head==None:
            nn=dnode(d)
            self.head=nn
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        nn=dnode(d)
        itr.next=nn

    def pri(self):
        itr=self.head
        while itr:
            print(itr.data,"->",end=" ")
            itr=itr.next
        print()

    def reverse(self):
        a=self.head
        itr=a.next
        a.next=None
        a.prev=itr

        while(itr.next):
            itr.prev=itr.next
            itr.next=a
            a=itr
            itr=itr.prev

        itr.next=a
        itr.prev=None
        self.head=itr

    def rev(self):
        a=self.head
        itr=a.next
        a.next=None
        a.prev=itr

        while itr:
            itr.prev=itr.next
            itr.next=a
            a=itr
            itr=itr.prev
        self.head=a

dll=DLL()
# dll.insertatstart(8)
# dll.insertatend(10)
dll.insertatend(3)
dll.insertatend(4)
dll.insertatend(5)
dll.insertatstart(1)
dll.pri()
dll.rev()
dll.reverse()
# print()
dll.pri()


