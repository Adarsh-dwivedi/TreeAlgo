class Node(object):

    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None

    def insert(self, data):
        #checking the condition acc to bst
        if data < self.data:
            if self.leftChild:  #if leftchild is present
                self.leftChild.insert(data)
            else:  #if left child is not present
                self.leftChild = Node(data)

        elif data > self.data:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)

    def remove(self, dataToRemove, parentNode):
        #checking the condition acc to bst
        if dataToRemove < self.data:
            if self.leftChild:  #if left child is present
                self.leftChild.remove(dataToRemove, self)

        elif dataToRemove > self.data :
            if self.rightChild:  #if right child is present
                self.rightChild.remove(dataToRemove, self)

        elif self.data == dataToRemove:
            if self.leftChild and self.rightChild:  #deleting node with two child
                self.data = self.rightChild.get_min()  #getting the minimum value from the right subtree of current object
                self.rightChild.remove(self.data, self)  #finding that node in right subtree to delete

            #deleting node with on child or no child
            elif parentNode.leftChild == self:  #deleting left child node or node with no child
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.leftChild = tempNode

            elif parentNode.rightChild == self:  #deleting right child node or node with no child
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.rightChild = tempNode


    def get_min(self):
        if self.leftChild:
            return self.leftChild.get_min()
        else:
            return self.data

    def get_max(self):
        if self.rightChild:
            return self.rightChild.get_max()
        else:
            return self.data

    def inorderTraverse(self):
        if self.leftChild:
            self.leftChild.inorderTraverse()

        print(self.data)

        if self.rightChild:
            self.rightChild.inorderTraverse()

