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
    def test_search(self):

        """
        not checking insertion here, creating an avl manually
        draw of the checked tree
                       d(3)
            b(1)               e(4)
        a(0)       c(2)               f(5)
        """

        tree = AVLTreeList()
        self.assertEqual(-1, tree.search("check"))
        root = AVLNode("d")
        tree.root = root
        node_b = AVLNode("b")
        root.setLeft(node_b)
        node_b.setParent(root)
        node_a = AVLNode("a")
        node_a.setParent(node_b)
        node_b.setLeft(node_a)
        node_c = AVLNode("c")
        node_c.setParent(node_b)
        node_b.setRight(node_c)
        node_e = AVLNode("e")
        root.setRight(node_e)
        node_e.setParent(root)
        node_f = AVLNode("f")
        node_f.setParent(node_e)
        node_e.setRight(node_f)
        root.setHeight(2)
        node_b.setHeight(1)
        node_e.setHeight(1)
        node_f.setHeight(0)
        node_c.setHeight(0)
        node_a.setHeight(0)
        self.assertEqual(0, tree.search("a"))
        self.assertEqual(1, tree.search("b"))
        self.assertEqual(2, tree.search("c"))
        self.assertEqual(3, tree.search("d"))
        self.assertEqual(4, tree.search("e"))
        self.assertEqual(5, tree.search("f"))
        self.assertEqual(-1, tree.search("A"))

    def test_predecessor(self):
        tree = AVLTreeList()
        root = AVLNode("d")
        self.assertEqual(None, tree.predecessor(root))
        tree.root = root
        node_b = AVLNode("b")
        root.setLeft(node_b)
        node_b.setParent(root)
        node_a = AVLNode("a")
        node_a.setParent(node_b)
        node_b.setLeft(node_a)
        node_c = AVLNode("c")
        node_c.setParent(node_b)
        node_b.setRight(node_c)
        node_1 = AVLNode("1")
        node_1.setParent(node_a)
        node_a.setRight(node_1)
        node_2 = AVLNode("2")
        node_2.setParent(node_c)
        node_c.setLeft(node_2)
        node_3 = AVLNode("3")
        node_3.setParent(node_c)
        node_c.setRight(node_3)
        node_f = AVLNode("f")
        node_f.setParent(root)
        root.setRight(node_f)
        node_e = AVLNode("e")
        node_e.setParent(node_f)
        node_f.setLeft(node_e)
        node_g = AVLNode("g")
        node_g.setParent(node_f)
        node_f.setRight(node_g)
        node_4 = AVLNode("4")
        node_4.setParent(node_e)
        node_e.setLeft(node_4)
        node_5 = AVLNode("5")
        node_5.setParent(node_g)
        node_g.setLeft(node_5)
        node_6 = AVLNode("6")
        node_6.setParent(node_g)
        node_g.setRight(node_6)
        node_1.setHeight(0)
        node_2.setHeight(0)
        node_3.setHeight(0)
        node_4.setHeight(0)
        node_5.setHeight(0)
        node_6.setHeight(0)
        node_a.setHeight(1)
        node_c.setHeight(1)
        node_e.setHeight(1)
        node_g.setHeight(1)
        node_b.setHeight(2)
        node_f.setHeight(2)
        root.setHeight(3)
        tree.set_First(node_a)
        tree.set_Last(node_6)
        self.assertEqual(None, tree.predecessor(node_a))
        self.assertEqual(node_a, tree.predecessor(node_1))
        self.assertEqual(node_1, tree.predecessor(node_b))
        self.assertEqual(node_b, tree.predecessor(node_2))
        self.assertEqual(node_2, tree.predecessor(node_c))
        self.assertEqual(node_c, tree.predecessor(node_3))
        self.assertEqual(node_3, tree.predecessor(root))
        self.assertEqual(root, tree.predecessor(node_4))
        self.assertEqual(node_4, tree.predecessor(node_e))
        self.assertEqual(node_e, tree.predecessor(node_f))
        self.assertEqual(node_f, tree.predecessor(node_5))
        self.assertEqual(node_5, tree.predecessor(node_g))
        self.assertEqual(node_g, tree.predecessor(node_6))

    def test_first_SetFirst(self):
        tree = AVLTreeList()




    if __name__ == "__main__":
        unittest.main()