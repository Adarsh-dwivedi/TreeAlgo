from AVLds.AvlNode import Node

class AVL(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):

        if self.rootNode is None:  #if tree is empty
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data, self)

    def inorderTraverse(self):
        if self.rootNode:  #if there is tree
            self.rootNode.inorderTraverse()
        else:
            print("Tree is empty")

    def height(self):
        if self.rootNode is None:
            print("Tree is empty")
        else:
            return self.rootNode.height()

    def remove(self, dataToRemove):
        if self.rootNode:
            if self.rootNode.data == dataToRemove:
                tempNode = Node(None)  #so that this node is become the parent of root node as we are passing the parentNode in remove
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(dataToRemove, tempNode, self)  #self is sending because so that we can change the rootNode after rotation
            else:
                self.rootNode.remove(dataToRemove, None, self)
        else:
            print("Tree is empty")
