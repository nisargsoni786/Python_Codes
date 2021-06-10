class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def addchild(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left=node(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right=node(data)

    def pri(self):
        if self.left:
            self.left.pri()
        print(self.data,end=" ")
        if(self.right):
            self.right.pri()

    def search(self,val):
        if self.data==val:
            return True
        if val>self.data:
            if self.right:
                return self.right.search(val)
        if val<self.data:
            if self.left:
                return self.left.search(val)
        return False

    def findmin(self):
        a=self
        while(a.right):
            a=a.right
        print(a.data)

    def summ(self):
        if self.left==None and self.right==None:
            return self.data
        elif self.left==None:
            return self.data+self.right.summ()
        elif self.right==None:
            return self.data+self.left.summ()
        else:
            return self.data+self.left.summ()+self.right.summ()

    def minval(self):
        if self.left:
            return self.left.minval()
        else:
            return self.data

    def delete(self,val):
        if val > self.data:
            if self.right:
                self.right=self.right.delete(val)
        if val < self.data:
            if self.left:
                self.left= self.left.delete(val)
        else:
            if self.left==None and self.right==None:
                return None
            if self.right==None:
                return self.left
            if self.left==None:
                return self.right

            min_value=self.right.minval()
            self.data=min_value
            self.right=self.right.delete(min_value)

        return self

def height(node):
    if node is None:
        return 0
    else:
        lh=height(node.left)
        rh=height(node.right)

        if lh > rh:
            return lh+1
        else:
            return rh+1

def levelorderpri(node):
    h=height(node)
    for i in range(1,h+1):
        prigivenlevel(node,i)

def prigivenlevel(root,lvl):
    if root is None:
        return
    if lvl==1:
        print(root.data,end=" ")
    elif(lvl >1):
        prigivenlevel(root.left,lvl-1)
        prigivenlevel(root.right,lvl-1)


if __name__=='__main__':
    root=node(17)
    #root.addchild(17)
    root.addchild(4)
    root.addchild(1)
    root.addchild(20)
    root.addchild(9)
    root.addchild(23)
    root.addchild(18)
    root.addchild(34)
    root.pri()
    print(root.search(21))
    root.findmin()
    print(root.summ())
    root.delete(17)
    root.pri()
    print()
    print(height(root))
    levelorderpri(root)










