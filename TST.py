from TernarySearchTree.TernaryNode import Node


class TST(object):

    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self._put_item(self.rootNode, key, value, 0)

    def _put_item(self, node, key, value, index):

        c = key[index]

        if node is None:
            node = Node(c)

        if c < node.character:
            node.leftChild = self._put_item(node.leftChild, key, value, index)

        elif c > node.character:
            node.rightChild = self._put_item(node.rightChild, key, value, index)

        elif index < len(key) - 1:
            node.middleChild = self._put_item(node.middleChild, key, value, index + 1)

        else:
            node.endString = 1
            node.value = value

        return node

    def get(self, key):
        node = self._get_item(self.rootNode, key, 0)

        if node is None:
            return "Not Found"

        if node.endString:
            return node.value
        else:
            return "Not Found"

    def _get_item(self, node, key, index):
        if node is None:
            return None

        c = key[index]

        if c < node.character:
            return self._get_item(node.leftChild, key, index)

        elif c > node.character:
            return self._get_item(node.rightChild, key, index)

        elif index < len(key) - 1:
            return self._get_item(node.middleChild, key, index + 1)

        else:
            return node
