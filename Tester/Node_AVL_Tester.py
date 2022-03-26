import unittest
import avl_skeleton as file
from avl_skeleton import AVLNode

class Test_Node_AVL(unittest.TestCase):
    def test_getHeight_setHeight(self):
        node = AVLNode(3)
        self.assertEqual(-1, node.getHeight())
        node.setHeight(5)
        self.assertEqual(5, node.getHeight())
        node.setValue(None)
        self.assertEqual(5, node.getHeight())
        node.setHeight(-1)
        self.assertEqual(-1, node.getHeight())


    def test_setValue(self):
        node = AVLNode(3)
        self.assertEqual(None, node.getValue())
        node.setHeight(4)
        self.assertEqual(3, node.getValue())
        node.setValue(5)
        self.assertEqual(5, node.getValue())

    def test_getLeft_setLeft(self):
        node = AVLNode("3")
        self.assertEqual(None, node.getLeft())
        lSon = AVLNode("2")
        node.setLeft(lSon)
        self.assertEqual(lSon, node.getLeft())
        l2Son = AVLNode("1")
        lSon.setLeft(l2Son)
        self.assertEqual(l2Son, lSon.getLeft())
        self.assertEqual(l2Son, node.getLeft().getLeft())

    def test_getRight_setRight(self):
        node = AVLNode("3")
        self.assertEqual(None, node.getRight())
        RSon = AVLNode("2")
        node.setRight(RSon)
        self.assertEqual(RSon, node.getRight())
        R2Son = AVLNode("1")
        RSon.setRight(R2Son)
        self.assertEqual(R2Son, RSon.getRight())
        self.assertEqual(R2Son, node.getRight().getRight())

    def test_getParent_setParent(self):
        node = AVLNode("3")
        self.assertEqual(None, node.getParent())
        p = AVLNode("Parent")
        node.setParent(p)
        self.assertEqual(p, node.getParent())
        l = AVLNode("Left")
        node.setLeft(l)
        l.setParent(node)
        self.assertEqual(node, l.getParent())
        self.assertEqual(p, l.getParent().getParent())
        r = AVLNode("Right")
        node.setRight(r)
        self.assertEqual(None,r.getParent())

    def test_getValue(self):
        node = AVLNode(3)
        self.assertEqual(None, node.getValue())
        node.setHeight(2)
        self.assertEqual(3, node.getValue())
        virtual = AVLNode(None)
        self.assertEqual(None, virtual.getValue())
        virtual.setHeight(5)
        self.assertEqual(None, virtual.getValue())
        l = AVLNode("Left")
        r = AVLNode("Right")
        node.setLeft(l)
        node.setRight(r)
        self.assertEqual(None, node.getLeft().getValue())
        self.assertEqual(None, node.getRight().getValue())
        l.setHeight(15)
        r.setHeight(15)
        self.assertEqual("Left", node.getLeft().getValue())
        self.assertEqual("Right", node.getRight().getValue())
        r.setParent(node)
        self.assertEqual(3, r.getParent().getValue())
        l.setParent(node)
        self.assertEqual(3, l.getParent().getValue())


    def test_isRealNode(self):
        node = AVLNode("3")
        self.assertEqual(False, node.isRealNode())
        node.setValue(None)
        self.assertEqual(False, node.isRealNode())
        lSon = AVLNode("2")
        node.setLeft(lSon)
        self.assertEqual(False, node.isRealNode())
        node.setValue("3")
        self.assertEqual(False, node.isRealNode())
        new_n = AVLNode(None)
        self.assertEqual(False, new_n.isRealNode())
        node.setHeight(2)
        self.assertEqual(True, node.isRealNode())
        node.setLeft(None)
        self.assertEqual(True, node.isRealNode())

    def test_getBalanceFactor(self):
        node = AVLNode("3")
        node.setHeight(1) # just so it won't be considered as virtual node
        lSon = AVLNode("2")
        node.setLeft(lSon)
        rSon = AVLNode("1")
        node.setRight(rSon)
        # Test Case 1: both sons are virtual. expected BF: 0.
        self.assertEqual(0, node.getBalanceFactor())
        # Test Case 2: left son is virtual & right son's height is 0. expected BF: -1.
        rSon.setHeight(0)
        self.assertEqual(-1, node.getBalanceFactor())
        # Test Case 3: right son is virtual & left son's height is 0. expected BF: 1.
        rSon.setHeight(-1)
        lSon.setHeight(0)
        self.assertEqual(1, node.getBalanceFactor())
        # Test Case 4: left son is virtual & right son's height is 1. expected BF: -2.
        lSon.setHeight(-1)
        rSon.setHeight(1)
        self.assertEqual(-2, node.getBalanceFactor())
        # Test Case 5: right son is virtual & left son's height is 1. expected BF: 2.
        rSon.setHeight(-1)
        lSon.setHeight(1)
        self.assertEqual(2, node.getBalanceFactor())

    if __name__ == "__main__":
        unittest.main()
