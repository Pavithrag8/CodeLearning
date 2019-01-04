
class Node:
    def __init__(self, val, left=None, right=None):

        self.left = left
        self.right = right
        self.val = val
        self.ser_data = ""

    def insert(self, val):
        if self.val:
            if val <= self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def serialize(self, root):
        inorder_ser = []
        if root:
            inorder_ser = self.serialize(root.left)
            inorder_ser.append(root.val)
            inorder_ser = inorder_ser + self.serialize(root.right)
        return inorder_ser   

root = Node(7)
root.insert(34)
root.insert(87)
root.insert(25)
root.insert(19)
root.insert(52)
root.insert(52)
root.insert(44)
root.insert(27)
root.insert(67)
root.insert(28)
serialize_data= root.serialize(root)
print "serialze data",serialize_data

#deserialize 
root = Node(serialize_data[0])
serialize_data.pop(0)
for val in serialize_data:
    root.insert(val)

