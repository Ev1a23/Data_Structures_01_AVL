import math

from avl_skeleton import AVLNode, AVLTreeList
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