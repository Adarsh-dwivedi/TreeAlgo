from BinarySearchTreeDS.BinaryNode import Node

class BST(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToRemove):
        if self.rootNode:
            if self.rootNode.data == dataToRemove:
                tempNode = Node(None)  #so that this node is become the parent of root node as we are passing the parentNode in remove
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(dataToRemove, tempNode)
            else:
                self.rootNode.remove(dataToRemove, None)
        else:
            print("Tree is empty")

    def get_max(self):
        if self.rootNode:
            return self.rootNode.get_max()
        else:
            print("Tree is empty")

    def get_min(self):
        if self.rootNode:
            return self.rootNode.get_min()
        else:
            print("Tree is empty")

    def inorderTraverse(self):
        if self.rootNode:
            self.rootNode.inorderTraverse()
        else:
            print("Tree is empty")
