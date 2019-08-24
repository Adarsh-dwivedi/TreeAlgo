class Node(object):

    def __init__(self, data):
        self.__leftChild = None
        self.data = data
        self.__rightChild = None
        self.__parentNode = None  #during rortation we have an access of parent node
        #self.__height = 0

    def insert(self, data, Aob):  #here Aob is AVL object so that we can change the root node if needed in rotation
        if data < self.data:
            if self.__leftChild is None:
                self.__leftChild = Node(data)
                self.__leftChild.__parentNode = self  #setting the parent node
                self.__leftChild._insertInspection(Aob)  #checking balance factor after every insertion
            else:
                self.__leftChild.insert(data, Aob)

        elif data > self.data:
            if self.__rightChild is None:
                self.__rightChild = Node(data)
                self.__rightChild.__parentNode = self
                self.__rightChild._insertInspection(Aob)  #checking balance factor after every insertion
            else:
                self.__rightChild.insert(data, Aob)

        else:
            print("data is already present")

    def height(self, curNode):
        if curNode is None:
            return -1

        leftHeight = self.height(curNode.__leftChild)
        rightHeight = self.height(curNode.__rightChild)

        return max(leftHeight, rightHeight)+1

    def _insertInspection(self, Aob, path = None):
        if self.__parentNode == None:  #this indicate that we reached the root node
            return

        if path is None: #path is used to store the reference of current and it's use in rebalance method
            path = []
        path.insert(0, self)

        leftHeight = self.__parentNode.height(self.__parentNode.__leftChild)
        rightHeight = self.__parentNode.height(self.__parentNode.__rightChild)

        if abs(leftHeight - rightHeight) > 1:
            self.__parentNode._rebalance(path[0], path[1], Aob)  #here we are passing the first unbalance node i.e self.__parentNode and two following Node
            return  #only one rotation is sufficient

        self.__parentNode._insertInspection(Aob, path)

    def _rebalance(self, parent, child1, Aob):
        if self.__rightChild == parent and parent.__rightChild == child1:
            self._leftRotate(Aob)
        elif self.__leftChild == parent and parent.__leftChild == child1:
            self._rightRotate(Aob)
        elif self.__leftChild == parent and parent.__rightChild == child1:
            parent._leftRotate(Aob)
            self._rightRotate(Aob)
        elif self.__rightChild == parent and parent.__leftChild == child1:
            parent._rightRotate(Aob)
            self._leftRotate(Aob)
        else:
            raise Exception('_rebalance_node: self, parent, child1 node configuration not recognized!')

    def _leftRotate(self, Aob):
        leftCh = self.__rightChild.__leftChild  #if we rotate left then refernece of left child get lost
        self.__rightChild.__leftChild = self

        if self.__parentNode is not None:  #it is not root node
            if self.__parentNode.__leftChild == self:  #cuurnt node is in the left of it's parent node
                self.__parentNode.__leftChild = self.__rightChild
            else:
                self.__parentNode.__rightChild = self.__rightChild  #current node is in the right of it's parent node
            self.__rightChild.__parentNode = self.__parentNode
        else:
            Aob.rootNode = self.__rightChild
            self.__rightChild.__parentNode = None
        self.__parentNode = self.__rightChild
        self.__rightChild = leftCh
        if leftCh is not None:  #changing the parent of it's left child
            leftCh.__parentNode = self

    def _rightRotate(self, Aob):
        rightCh = self.__leftChild.__rightChild
        self.__leftChild.__rightChild = self
        if self.__parentNode is not None:
            if self.__parentNode.__leftChild == self:
                self.__parentNode.__leftChild = self.__leftChild
            else:
                self.__parentNode.__rightChild = self.__leftChild
            self.__leftChild.__parentNode = self.__parentNode
        else:
            Aob.rootNode = self.__leftChild
            self.__leftChild.__parentNode = None

        self.__parentNode = self.__leftChild
        self.__leftChild = rightCh
        if rightCh is not None:
            rightCh.__parentNode = self

    def inorderTraverse(self):
        if self.__leftChild:
            self.__leftChild.inorderTraverse()

        print(self.data)

        if self.__rightChild:
            self.__rightChild.inorderTraverse()

    def remove(self, dataToRemove, parentNode, Aob):
        #checking the condition acc to bst
        if dataToRemove < self.data:
            if self.__leftChild:  #if left child is present
                self.__leftChild.remove(dataToRemove, self, Aob)

        elif dataToRemove > self.data :
            if self.__rightChild:  #if right child is present
                self.__rightChild.remove(dataToRemove, self, Aob)

        elif self.data == dataToRemove:
            if self.__leftChild and self.__rightChild:  #deleting node with two child
                self.data = self.__rightChild.get_min()  #getting the minimum value from the right subtree of current object
                self.__rightChild.remove(self.data, self, Aob)  #finding that node in right subtree to delete

            #deleting node with on child or no child
            elif parentNode.__leftChild == self:  #deleting left child node or node with no child
                if self.__leftChild is not None:
                    tempNode = self.__leftChild
                else:
                    tempNode = self.__rightChild

                parentNode.__leftChild = tempNode
                if tempNode is not None:
                    tempNode.__parentNode = parentNode
                if self.__parentNode is not None:
                    self._inspectDeletion(parentNode, Aob)

            elif parentNode.__rightChild == self:  #deleting right child node or node with no child
                if self.__leftChild is not None:
                    tempNode = self.__leftChild
                else:
                    tempNode = self.__rightChild

                parentNode.__rightChild = tempNode
                if tempNode is not None:
                    tempNode.__parentNode = parentNode
                if self.__parentNode is not None:
                    self._inspectDeletion(parentNode, Aob)

    def _inspectDeletion(self, curNode, Aob):
        if curNode is None: #we are at the parent of root node
            return

        leftHeight = curNode.height(curNode.__leftChild)
        rightHeight = curNode.height(curNode.__rightChild)

        if abs(leftHeight - rightHeight) > 1:
            parent = self.findChild(curNode)  #finding two other node
            child1 = self.findChild(parent)
            curNode._rebalance(parent, child1, Aob)

        self._inspectDeletion(curNode.__parentNode, Aob)

    def findChild(self, curNode):

        left = self.height(curNode.__leftChild)
        right = self.height(curNode.__rightChild)

        #if height of the left child is more than there is one more node than the right child

        return curNode.__leftChild if left >= right else curNode.__rightChild

    def get_min(self):
        if self.__leftChild:
            return self.__leftChild.get_min()
        else:
            return self.data