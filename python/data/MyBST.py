class Node(object):

    def __init__(self, d):
        self.d = d
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.d)
"""
This is an implemantation for Binary Search Tree
"""
class MyBST(object):
    def __init__(self):
        self.root = None

    def insert(self, n):
        if self.root == None:
            self.root = Node(n)
        else:
            current = self.root
            while current != None:
                if n < current.d:
                    if current.left == None:
                        current.left = Node(n)
                        break
                    else:
                        current = current.left
                elif n > current.d:
                    if current.right == None:
                        current.right = Node(n)
                        break
                    else:
                        current = current.right
                else:
                    break

    def find(self, n):
        current = self.root
        while current != None:
            if current.d == n:
                return True
            if n>current.d:
                current = current.right
            elif n<current.d:
                current = current.left
        return False

    def preorder_print(self):
        return self.preorder_print_(self.root)


    def preorder_print_(self, n):
        if n == None:
            return 

        print n.d
        self.preorder_print_(n.left)
        self.preorder_print_ (n.right) 

    def inorder_print(self):
        return self.inorder_print_(self.root)


    def inorder_print_(self, n):
        if n == None:
            return 

        self.inorder_print_(n.left)
        print n.d
        self.inorder_print_ (n.right) 


if __name__ == '__main__':  
    bst = MyBST()

    for x in [ 100,50,25,75,10, 200,150, 167 ]:
        bst.insert(x)

    bst.inorder_print()    