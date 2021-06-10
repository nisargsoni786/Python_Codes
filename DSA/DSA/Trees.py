class treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def addchild(self,child):
        child.parent=self
        self.children.append(child)

    def pri(self):
        print(self.data)
        if self.children:
            for i in self.children:
                print("      ",end="")
                i.pri()

def buildtree():
    root=treenode("elec")
    laptop=treenode('lappy')
    lap1=treenode('lap1')
    lap2=treenode('lap2')
    laptop.addchild(lap1) 
    laptop.addchild(lap2)
    kiki=treenode('kiki')
    root.addchild(laptop)
    root.addchild(kiki)
    return root

if __name__=='__main__':
    root=buildtree()
    root.pri()
