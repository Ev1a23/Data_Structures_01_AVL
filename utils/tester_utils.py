import math

from AVLTreeList import AVLNode, AVLTreeList
from utils.print_tree import printTreefinal


def setFirst(tree):
    first = tree.getRoot()
    while first.getLeft().isRealNode():
        first = first.getLeft()
    tree.set_First(first)


def setLast(tree):
    last = tree.getRoot()
    while last.getRight().isRealNode():
        last = last.getRight()
    tree.set_Last(last)

# setFields(node, lst[i], AVLNode(None), AVLNode(None), None, 0, 1)
#
# node.setFields(node, lst[i], left, right, None, max(left.getHeight(), right.getHeight()) + 1,
#                    left.getSize() + right.getSize() + 1)


def setFields(node, value, left, right, parent, height, size):
    node.setValue(value)
    node.setLeft(left)
    node.setRight(right)
    node.setParent(parent)
    node.setHeight(height)
    node.setSize(size)


"""This method is for testing ONLY and returns a legal tree based in a given list
@pre: list of strings which satisfies the following format: (examples ahead)
	list length is a power of 2 minus 1 and
	index 0 is the root
    next 2 indexes are the sons of the root,
	next 4 indexes are the sons of the root's sons, from left to right
    next 8 ...
	and so on by this pattern while a "missing son" will be represented by None
@post: False if list represents illegal tree, compatible AVLTreeList otherwise
@rtype: AVLTreeList

examples:
The list ['a','b','c','d','e',None,'f'] will create the following tree
(including virtual sons which are not detailed here)
             a
          /     \
        b         c
      /   \         \
     d     e         f

The list ['a','None','c',None, None, None, 'f'] will return False 
because it represents an illegal tree:
             a
                \
                  c
                    \
                     f
"""


def createTreeFromList(lst):
    if len(lst) == 0:
        return AVLTreeList()
    if math.log(len(lst) + 1, 2) % 1 != 0:
        return False
    tree = AVLTreeList()
    root = createTreeFromList_rec(lst, 0, 0)
    tree.root = root
    setFirst(tree)
    setLast(tree)
    return tree


def createTreeFromList_rec(lst, i, power):
    if (lst[i] == None):
        # return virtual Node from lst[i]:
        return AVLNode(lst[i])

    ##calc next index of left son's index, right son will be the following index:
    nextIndex = i + 2 ** power + (i + 1) - 2 ** (math.floor(math.log(i + 1, 2)))

    if nextIndex >= len(lst):
        node = AVLNode(None)
        setFields(node, lst[i], AVLNode(None), AVLNode(None), None, 0, 1)
        node.getLeft().setParent(node)
        node.getRight().setParent(node)
        return node

    left = createTreeFromList_rec(lst, nextIndex, power + 1)
    right = createTreeFromList_rec(lst, nextIndex + 1, power + 1)

    node = AVLNode(lst[i])
    setFields(node, lst[i], left, right, None, max(left.getHeight(), right.getHeight()) + 1,
                   left.getSize() + right.getSize() + 1)
    left.setParent(node)
    right.setParent(node)
    return node


def createAVLTreeFromList(lst):
    if len(lst) == 0:
        return AVLTreeList()
    if math.log(len(lst) + 1, 2) % 1 != 0:
        return False
    tree = AVLTreeList.AVLTreeList()
    root = createTreeFromList_rec(lst, 0, 0)
    if root.height > -2:
        tree.root = root
        setFirst(tree)
        setLast(tree)
        return tree

    else:
        print("list does not represent a valid tree")
        return False


def createAVLTreeFromList_rec(lst, i, power):
    if (lst[i] == None):
        # return virtual Node from lst[i]:
        return AVLNode(lst[i])

    ##calc next index of left son's index, right son will be the following index:
    nextIndex = i + 2 ** power + (i + 1) - 2 ** (math.floor(math.log(i + 1, 2)))

    if nextIndex >= len(lst):
        node = AVLNode(None)
        setFields(node, lst[i], AVLTreeList.AVLNode(None), AVLTreeList.AVLNode(None), None, 0, 1)
        node.getLeft().setParent(node)
        node.getRight().setParent(node)
        return node

    left = createTreeFromList_rec(lst, nextIndex, power + 1)
    right = createTreeFromList_rec(lst, nextIndex + 1, power + 1)
    if left.getHeight() > -2 and right.getHeight() > -2:
        if abs(right.height - left.height) > 1:
            node = AVLNode(None)
            node.setHeight(-2)
            return node

        else:
            node = AVLNode(lst[i])
            setFields(node, lst[i], left, right, None, max(left.getHeight(), right.getHeight()) + 1,
                           left.getSize() + right.getSize() + 1)
            left.setParent(node)
            right.setParent(node)
            return node

    else:
        node = AVLNode(None)
        node.setHeight(-2)
        return node



"""
Create a tree from a list using insert operations, from the first to the last item
Only from testing
"""

def createTreeFromListInsert(lst):
    tree = AVLTreeList()
    for i in range(len(lst)):
        tree.insert(i, lst[i])
    return tree



""" comparing 2 nodes by:
height
size
value
parent's value
leftSon's value
rightSon's value

@type node1: AVLNode
@type node2: AVLNode
"""


def nodesEqual(node1, node2):
    if node2 is None and node1 is not None:
        return False
    if node1 is None and node2 is not None:
        return False
    if node1 is None and node2 is None:
        return True

    heightIsEqual = node1.getHeight() == node2.getHeight()
    sizeIsEqual = node1.getSize() == node2.getSize()
    valueIsEqual = node1.getValue() == node2.getValue()

    if node1.isRealNode() and not node2.isRealNode():
        return False
    if node2.isRealNode() and not node1.isRealNode():
        return False
    if not node1.isRealNode() and not node2.isRealNode():
        return node1.getParent().getValue() == node2.getParent().getValue() # not real nodes - compare their parent's values

    # by getting here we know that node1 and node2 are real nodes

    parentIsEqual = node1.getParent().getValue() == node2.getParent().getValue() if node1.getParent() is not None and node2.getParent() is not None else node1.getParent() is None and node2.getParent() is None
    leftSonIsEqual = node1.getLeft().getValue() == node2.getLeft().getValue() if node1.getLeft().isRealNode() and node2.getLeft().isRealNode() else node1.getLeft().isRealNode() == node2.getLeft().isRealNode()
    rightSonIsEqual = node1.getRight().getValue() == node2.getRight().getValue() if node1.getRight().isRealNode() and node2.getRight().isRealNode() else node1.getRight().isRealNode() == node2.getRight().isRealNode()

    return heightIsEqual and sizeIsEqual and valueIsEqual and parentIsEqual and leftSonIsEqual and rightSonIsEqual


"""Checks if current AVLTreeList is equals to another AVLTreeList
Definition: AVLTreeList are considered equal if trees size are equal 
and recursively checking that currentTreeRoot == otherTreeRoot (by checking their values, size, and height) 
& currentTreeRoot.left equals otherTreeRoot.left
& currentTreeRoot.right equals otherTreeRoot.right

@type other: AVLTreeList
@param other: an AVLTreeList to compare self to
@returns: True if trees are equal, False otherwise
@rtype: boolean
"""


def treesEqual(tree1, tree2):
    if (not isinstance(tree2, AVLTreeList)) or tree2.length() != tree1.length():
        return False

    currentRoot = tree1.getRoot()
    otherRoot = tree2.getRoot()

    if currentRoot is None and otherRoot is None:
        return True

    if not nodesEqual(tree1.get_First(), tree2.get_First()):
        return False

    if not nodesEqual(tree1.get_Last(), tree2.get_Last()):
        return False

    def equalsRec(currentNode, otherNode):
        if not currentNode.isRealNode() and not otherNode.isRealNode():
            return True

        if not nodesEqual(currentRoot, otherRoot):
            return False

        return equalsRec(currentNode.getLeft(), otherNode.getLeft()) and equalsRec(currentNode.getRight(),
                                                                                   otherNode.getRight())

    return equalsRec(currentRoot, otherRoot)
