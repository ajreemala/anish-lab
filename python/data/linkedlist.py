class Node(object):
    next = None
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return 'node: '+self.data

class LinkedList(object):
    head = None

    def __init__(self):
        pass

    def insert_front(self, node):
        if self.head == None:
            self.head=node
        else:
            node.next=self.head
            self.head = node

    def insert_back(self, node):
        pass

    def insert(self, node, index):
        if self.head == None:
            self.head=node
        else:
            current=head
            count = 0
            while current.next != None and count != index:
                current=current.next
                count=count+1




    def get(self, index):
        pass


    def __str__(self):
        t=self.head
        ret=[]
        while t != None:
            ret.append(str(t))
            t=t.next
        return str(ret)


if __name__=='__main__':
    l=LinkedList()
    z=Node('zip')
    l.insert(z)
    print str(l)
    a=Node('art')
    l.insert(a)
    l.insert(Node('xyz'))
    print str(l)
