import unittest
import avl_skeleton as file
from avl_skeleton import AVLNode
from avl_skeleton import AVLTreeList

class Test_AVL_Tree_list(unittest.TestCase):
    def test_Empty(self):
        tree = AVLTreeList()
        self.assertEqual(True, tree.empty())
        root = AVLNode("3")
        tree.root = root
        self.assertEqual(False, tree.empty())
        root.height = 3
        self.assertEqual(False, tree.empty())
        root.setValue(5)
        self.assertEqual(False, tree.empty())
        tree.root = None
        self.assertEqual(True, tree.empty())

    def test_GetRoot(self):
        tree = AVLTreeList()
        self.assertEqual(None, tree.getRoot())
        root = AVLNode("3")
        tree.root = root
        self.assertEqual(root, tree.getRoot())
        root.setValue("5")
        self.assertEqual(root, tree.getRoot())
        root2 = AVLNode("3")
        tree.root = root2
        self.assertEqual(root2, tree.getRoot())
        root2 = None
        self.assertNotEqual(None, tree.getRoot())

    def test_first_getFirst_setFirst(self):
        tree = AVLTreeList()
        self.assertEqual(None, tree.get_First())
        self.assertEqual(None, tree.first())
        root = AVLNode("root")
        root.setHeight(5)
        tree.root = root
        tree.set_First(root)
        self.assertEqual("root", tree.first())
        right = AVLNode("first")
        right.setHeight(5)
        root.setLeft(right)
        tree.set_First(right)
        self.assertEqual("first", tree.first())
        self.assertEqual(right, tree.get_First())

    def test_last_getLast_setLast(self):
        tree = AVLTreeList()
        self.assertEqual(None, tree.get_Last())
        self.assertEqual(None, tree.last())
        root = AVLNode("root")
        root.setHeight(5)
        tree.root = root
        tree.set_Last(root)
        self.assertEqual("root", tree.last())
        right = AVLNode("last")
        right.setHeight(5)
        root.setRight(right)
        tree.set_Last(right)
        self.assertEqual("last", tree.last())
        self.assertEqual(right, tree.get_Last())


    if __name__ == "__main__":
        unittest.main()