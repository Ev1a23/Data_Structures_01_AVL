import sys
import unittest
from avl_skeleton import AVLNode
from avl_skeleton import AVLTreeList
from utils.tester_utils import createTreeFromList, treesEqual, nodesEqual, setFields, createTreeFromListInsert
from utils.print_tree import printTreeString
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(funcName)s - line %(lineno)s: %(levelname)s] %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


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

        ## Using function to build trees from list

        tree_fromList = createTreeFromList([])
        self.assertEqual(True, tree_fromList.empty())
        root = AVLNode("3")
        tree_fromList.root = root
        self.assertEqual(False, tree_fromList.empty())
        root.height = 3
        self.assertEqual(False, tree_fromList.empty())
        root.setValue(5)
        self.assertEqual(False, tree_fromList.empty())
        tree_fromList.root = None
        self.assertEqual(True, tree_fromList.empty())

    def test_length(self):
        tree = AVLTreeList()

        # Test Case 1: root is None. expected length: 0.
        self.assertEqual(0, tree.length())

        # Test Case 2: root is not None, size of root is 10. expected length: 10.
        root = AVLNode("3")
        root.setSize(10)
        tree.root = root
        self.assertEqual(10, tree.length())

    def test_retrieve(self):
        tree = AVLTreeList()
        root = AVLNode("3")
        root.setSize(1)
        root.setHeight(0)
        lSon = AVLNode("2")
        rSon = AVLNode("4")
        root.setLeft(lSon)
        root.setRight(rSon)
        tree.root = root

        # Test Case 1: tree has only 1 node - root. i = 0. expected: root.
        #         root
        #        /    \
        #       ---   ---
        self.assertEqual(root.getValue(), tree.retrieve(0))

        # Test Case 2: tree has a root and a left node which is a leaf.
        #              root
        #           /        \
        #          l         ---
        #        /    \
        #       ---  ---
        # i = 0. expected: left son.
        # i = 1. expected: root.
        lSon.setHeight(0)
        lSon.setSize(1)
        llSon = AVLNode("3")
        lSon.setLeft(llSon)
        root.setSize(2)
        self.assertEqual(lSon.getValue(), tree.retrieve(0))
        self.assertEqual(root.getValue(), tree.retrieve(1))

        # Test Case 3: tree has a root and a right node which is a leaf.
        #             root
        #           /      \
        #         ---        r
        #                  /    \
        #                 ---  ---
        # i = 0. expected: root.
        # i = 1. expected: right son.
        lSon.setHeight(-1)
        lSon.setSize(0)
        rSon.setHeight(0)
        rSon.setSize(1)
        self.assertEqual(root.getValue(), tree.retrieve(0))
        rlSon = AVLNode("4")
        rSon.setLeft(rlSon)
        self.assertEqual(rSon.getValue(), tree.retrieve(1))

        # Test Case 4: tree has a root and a left son that has a left son.
        #                        root
        #                     /       \
        #                   l         ---
        #                 /   \
        #               ll     ---
        #             /   \
        #           ---   ---
        # i = 0. expected: most left son of root.
        # i = 1. expected: left son of root.
        # i = 2. expected: root.
        lllSon = AVLNode("3")
        llSon.setLeft(lllSon)
        llSon.setHeight(0)
        llSon.setSize(1)
        lSon.setSize(2)
        root.setSize(3)
        rSon.setHeight(-1)
        self.assertEqual(llSon.getValue(), tree.retrieve(0))
        self.assertEqual(lSon.getValue(), tree.retrieve(1))
        self.assertEqual(root.getValue(), tree.retrieve(2))

        # Test Case 5: tree has a root and a right son that has a right son.
        #                        root
        #                     /       \
        #                   ---         r
        #                             /   \
        #                            ---   rr
        #                                /    \
        #                              ---    ---
        # i = 0. expected: root.
        # i = 1. expected: right son of root.
        # i = 2. expected: most right son of root.
        rrSon = AVLNode("3")
        rSon.setRight(rrSon)
        rrlSon = AVLNode("3")
        rrSon.setLeft(rrlSon)
        rrSon.setHeight(0)
        rrSon.setSize(1)
        rSon.setSize(2)
        root.setSize(3)
        lSon.setHeight(-1)
        lSon.setSize(0)
        self.assertEqual(root.getValue(), tree.retrieve(0))
        self.assertEqual(rSon.getValue(), tree.retrieve(1))
        self.assertEqual(rrSon.getValue(), tree.retrieve(2))

        # Test Case 6:
        #                        root
        #                     /       \
        #                   l           r
        #                 /   \       /   \
        #               ----   lr    -------
        #                    /   \
        #                   -------
        # i = 0. expected: l.
        # i = 1. expected: lr.
        # i = 2. expected: root.
        # i = 3. expected: r.
        virtualNode = AVLNode("1")
        rSon.setHeight(0)
        rSon.setSize(1)
        rSon.setLeft(virtualNode)
        rSon.setRight(virtualNode)

        lSon.setHeight(1)
        lSon.setSize(2)
        lSon.setLeft(virtualNode)

        lrSon = AVLNode("3")
        lrSon.setHeight(0)
        lrSon.setSize(1)
        lrSon.setLeft(virtualNode)
        lrSon.setRight(virtualNode)
        lSon.setRight(lrSon)

        root.setHeight(2)
        root.setSize(4)
        self.assertEqual(lSon.getValue(), tree.retrieve(0))
        self.assertEqual(lrSon.getValue(), tree.retrieve(1))
        self.assertEqual(root.getValue(), tree.retrieve(2))
        self.assertEqual(rSon.getValue(), tree.retrieve(3))

        # Test Case 7:
        #                        root
        #                     /       \
        #                   l           r
        #                 /   \       /   \
        #                -------    rl   ----
        #                          /   \
        #                         -------
        # i = 0. expected: l.
        # i = 1. expected: root.
        # i = 2. expected: rl.
        # i = 3. expected: r.
        lSon.setHeight(0)
        lSon.setSize(1)
        lSon.setLeft(virtualNode)
        lSon.setRight(virtualNode)

        rSon.setHeight(1)
        rSon.setSize(2)
        rSon.setRight(virtualNode)

        rlSon = AVLNode("3")
        rlSon.setHeight(0)
        rlSon.setSize(1)
        rlSon.setLeft(virtualNode)
        rlSon.setRight(virtualNode)
        rSon.setLeft(rlSon)

        root.setHeight(2)
        root.setSize(4)
        self.assertEqual(lSon.getValue(), tree.retrieve(0))
        self.assertEqual(root.getValue(), tree.retrieve(1))
        self.assertEqual(rlSon.getValue(), tree.retrieve(2))
        self.assertEqual(rSon.getValue(), tree.retrieve(3))

    def test_minimum(self):
        # Test Case 1: a Tree with one node
        #            root
        #          /      \
        #        ---      ---
        # expected: root.
        tree = AVLTreeList()
        root = AVLNode("3")
        root.setHeight(0)
        root.setSize(1)
        tree.root = root
        virtualNode = AVLNode("2")
        root.setLeft(virtualNode)
        root.setRight(virtualNode)
        self.assertEqual(root, tree.minimum(root))

        # Test Case 2: Node's left son is virtual, right son isn't virtual
        #            root
        #          /      \
        #        ---       r
        #                /   \
        #              ---   ---
        # expected: root
        rSon = AVLNode("3")
        rSon.setHeight(0)
        rSon.setSize(1)
        rSon.setRight(virtualNode)
        rSon.setLeft(virtualNode)
        root.setRight(rSon)
        root.setHeight(1)
        root.setSize(2)
        self.assertEqual(root, tree.minimum(root))

        # Test Case 3: Node's left son is a leaf, right son isn't virtual
        #            root
        #          /      \
        #         l        r
        #       /   \    /   \
        #     ---  --- ---   ---
        # expected: l
        lSon = AVLNode("3")
        lSon.setHeight(0)
        lSon.setSize(1)
        lSon.setRight(virtualNode)
        lSon.setLeft(virtualNode)
        root.setLeft(lSon)
        root.setHeight(1)
        root.setSize(3)
        self.assertEqual(lSon, tree.minimum(root))
        # Test Case 4: Node's left son has only a right son, right son isn't virtual
        #            root
        #          /      \
        #         l        r
        #       /   \    /   \
        #     ---   lr ---   ---
        #          /  \
        #        ---  ---
        # expected: l
        lrSon = AVLNode("3")
        lrSon.setHeight(0)
        lrSon.setSize(1)
        lrSon.setRight(virtualNode)
        lrSon.setLeft(virtualNode)
        lSon.setRight(lrSon)
        lSon.setHeight(1)
        lSon.setSize(2)
        root.setHeight(2)
        root.setSize(4)
        self.assertEqual(lSon, tree.minimum(root))

    def test_listToArray(self):
        tree = AVLTreeList()
        root = AVLNode("3")
        root.setSize(1)
        root.setHeight(0)
        lSon = AVLNode("2")
        rSon = AVLNode("4")
        virtualNode = AVLNode(None)
        root.setLeft(lSon)
        root.setRight(rSon)
        tree.root = root
        tree.set_First(root)

        # Test Case 1: tree has only 1 node - root. i = 0. expected: ["3"].
        #         root
        #        /    \
        #       ---   ---
        self.assertEqual(["3"], tree.listToArray())
        root.setValue("kk")
        self.assertEqual(["kk"], tree.listToArray())
        root.setValue("3")

        # Test Case 2: tree has a root and a left node which is a leaf.
        #              root
        #           /        \
        #          l         ---
        #        /    \
        #       ---  ---
        # expected: ["2","3"].
        lSon.setHeight(0)
        lSon.setSize(1)
        llSon = AVLNode("3")
        lSon.setLeft(llSon)
        lSon.setRight(virtualNode)
        root.setSize(2)
        lSon.setParent(root)
        tree.set_First(lSon)
        self.assertEqual(["2", "3"], tree.listToArray())

        # Test Case 3: tree has a root and a right node which is a leaf.
        #             root
        #           /      \
        #         ---        r
        #                  /    \
        #                 ---  ---
        # expected: ["3", "4"]
        lSon.setHeight(-1)
        lSon.setSize(0)
        rSon.setHeight(0)
        rSon.setSize(1)
        rSon.setLeft(virtualNode)
        rSon.setRight(virtualNode)
        tree.set_First(root)
        rSon.setParent(root)
        self.assertEqual(["3", "4"], tree.listToArray())
        rlSon = AVLNode("4")
        rSon.setLeft(rlSon)

        # Test Case 4: tree has a root and a left son that has a left son.
        #                        root
        #                     /       \
        #                   l         ---
        #                 /   \
        #               ll     ---
        #             /   \
        #           ---   ---
        # expected: ["3", "2", "3"]
        lllSon = AVLNode("3")
        llSon.setLeft(lllSon)
        llSon.setRight(virtualNode)
        llSon.setHeight(0)
        llSon.setSize(1)
        lSon.setSize(2)
        lSon.setHeight(1)
        root.setSize(3)
        rSon.setHeight(-1)
        llSon.setParent(lSon)
        tree.set_First(llSon)
        self.assertEqual(["3", "2", "3"], tree.listToArray())

        # Test Case 5: tree has a root and a right son that has a right son.
        #                        root
        #                     /       \
        #                   ---         r
        #                             /   \
        #                            ---   rr
        #                                /    \
        #                              ---    ---
        # expected: ["3", "4", "3"]
        rrSon = AVLNode("3")
        rSon.setRight(rrSon)
        rrlSon = AVLNode("3")
        rrSon.setLeft(rrlSon)
        rrSon.setHeight(0)
        rrSon.setSize(1)
        rSon.setSize(2)
        rSon.setHeight(1)
        root.setSize(3)
        lSon.setHeight(-1)
        lSon.setSize(0)
        rrSon.setParent(rSon)
        rrSon.setRight(AVLNode("2"))
        tree.set_First(root)
        self.assertEqual(["3", "4", "3"], tree.listToArray())

        # Test Case 6:
        #                        root
        #                     /       \
        #                   l           r
        #                 /   \       /   \
        #               ----   lr    -------
        #                    /   \
        #                   -------
        # expected: ["2", "3", "3", "4"]
        virtualNode = AVLNode("1")
        rSon.setHeight(0)
        rSon.setSize(1)
        rSon.setLeft(virtualNode)
        rSon.setRight(virtualNode)

        lSon.setHeight(1)
        lSon.setSize(2)
        lSon.setLeft(virtualNode)

        lrSon = AVLNode("3")
        lrSon.setHeight(0)
        lrSon.setSize(1)
        lrSon.setLeft(virtualNode)
        lrSon.setRight(virtualNode)
        lSon.setRight(lrSon)

        root.setHeight(2)
        root.setSize(4)
        tree.set_First(lSon)
        lrSon.setParent(lSon)
        self.assertEqual(["2", "3", "3", "4"], tree.listToArray())

        # Test Case 7:
        #                        root
        #                     /       \
        #                   l           r
        #                 /   \       /   \
        #                -------    rl   ----
        #                          /   \
        #                         -------
        # expected: ["2", "3", "4", "5"], changing r's value to "5"
        lSon.setHeight(0)
        lSon.setSize(1)
        lSon.setLeft(virtualNode)
        lSon.setRight(virtualNode)

        rSon.setHeight(1)
        rSon.setSize(2)
        rSon.setRight(virtualNode)
        rSon.setValue("5")

        rlSon = AVLNode("4")
        rlSon.setHeight(0)
        rlSon.setSize(1)
        rlSon.setLeft(virtualNode)
        rlSon.setRight(virtualNode)
        rSon.setLeft(rlSon)

        root.setHeight(2)
        root.setSize(4)
        rlSon.setParent(rSon)
        self.assertEqual(["2", "3", "4", "5"], tree.listToArray())

        # Test Case 8: tree is empty.
        #          ---
        emptyTree = AVLTreeList()
        tree.set_First(None)
        self.assertEqual([], emptyTree.listToArray())

    def test_successor(self):
        tree = AVLTreeList()
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
        virtualNode = AVLNode("3")
        node_6.setRight(virtualNode)
        node_e.setRight(virtualNode)
        node_1.setRight(virtualNode)
        node_2.setRight(virtualNode)
        node_3.setRight(virtualNode)
        node_4.setRight(virtualNode)
        node_5.setRight(virtualNode)
        node_6.setLeft(virtualNode)
        node_a.setLeft(virtualNode)
        node_1.setLeft(virtualNode)
        node_2.setLeft(virtualNode)
        node_3.setLeft(virtualNode)
        node_4.setLeft(virtualNode)
        node_5.setLeft(virtualNode)
        self.assertEqual(None, tree.successor(node_6))
        self.assertEqual(node_1, tree.successor(node_a))
        self.assertEqual(node_b, tree.successor(node_1))
        self.assertEqual(node_2, tree.successor(node_b))
        self.assertEqual(node_c, tree.successor(node_2))
        self.assertEqual(node_3, tree.successor(node_c))
        self.assertEqual(root, tree.successor(node_3))
        self.assertEqual(node_4, tree.successor(root))
        self.assertEqual(node_e, tree.successor(node_4))
        self.assertEqual(node_f, tree.successor(node_e))
        self.assertEqual(node_5, tree.successor(node_f))
        self.assertEqual(node_g, tree.successor(node_5))
        self.assertEqual(node_6, tree.successor(node_g))

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
        node_v1 = AVLNode("V1")
        node_v1.setParent(node_a)
        node_v2 = AVLNode("v2")
        node_v2.setParent(node_a)
        node_a.setRight(node_v2)
        node_a.setLeft(node_v1)
        node_b.setLeft(node_a)
        node_c = AVLNode("c")
        node_v3 = AVLNode("v3")
        node_v3.setParent(node_c)
        node_c.setLeft(node_v3)
        node_v4 = AVLNode("v4")
        node_v4.setParent(node_c)
        node_c.setRight(node_v4)
        node_c.setParent(node_b)
        node_b.setRight(node_c)
        node_e = AVLNode("e")
        root.setRight(node_e)
        node_e.setParent(root)
        node_v5 = AVLNode("v5")
        node_v5.setParent(node_e)
        node_e.setLeft(node_v5)
        node_f = AVLNode("f")
        node_f.setParent(node_e)
        node_e.setRight(node_f)
        node_v6 = AVLNode("v6")
        node_v6.setParent(node_f)
        node_f.setLeft(node_v6)
        node_v7 = AVLNode("v7")
        node_v7.setParent(node_f)
        node_f.setRight(node_v7)
        root.setHeight(2)
        node_b.setHeight(1)
        node_e.setHeight(1)
        node_f.setHeight(0)
        node_c.setHeight(0)
        node_a.setHeight(0)
        tree.set_First(node_a)
        tree.set_Last(node_f)
        root.setSize(6)
        node_b.setSize(3)
        node_a.setSize(1)
        node_c.setSize(1)
        node_e.setSize(2)
        node_f.setSize(1)
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

    def test_rightRotation(self):
        afterRightRotationMsg = "after right rotation"

        # Test case 1: right rotation when the root is the criminal
        rootCriminalTree = createTreeFromList(["a", "b", None, "c", None, None, None])
        logger.debug(f"Test case 1 - root 'a' is BF criminal\n{printTreeString(rootCriminalTree)}")
        criminal = rootCriminalTree.getRoot()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'right')

        rootCriminalTree.rightRotation(criminal)

        # Visual check
        logger.debug(f"Test case 1 - {afterRightRotationMsg}:\n{printTreeString(rootCriminalTree)}")
        # Pointers check
        self.rightRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.rightRotationFieldsCheck(nodesToCheck)
        # Undependent check
        expectedTree = createTreeFromList(["b", "c", "a", None, None, None, None])
        self.assertTrue(treesEqual(rootCriminalTree, expectedTree))

        # Test case 2: right rotation when some node is the criminal (BF of criminal.left == 1)
        test2Tree = createTreeFromList(["a", "b", "c", "d", None, "e", "f", "g", None, None, None, "i", "j", "k", "l"])
        logger.debug(f"Test case 2 - node 'b' is BF criminal\n{printTreeString(test2Tree)}")
        criminal = test2Tree.getRoot().getLeft()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'right')

        test2Tree.rightRotation(criminal)

        # Visual check
        logger.debug(f"Test case 2 - {afterRightRotationMsg}:\n{printTreeString(test2Tree)}")
        # Pointers check
        self.rightRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.rightRotationFieldsCheck(nodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(test2Tree, createTreeFromList(
            ["a", "d", "c", "g", "b", "e", "f", None, None, None, None, "i", "j", "k", "l"])))

        # Test case 3: right rotation when some node is the criminal (BF of criminal.left == 0)
        test2Tree = createTreeFromList(["a", "b", "c", "d", None, "e", "f", "g", "h", None, None, "i", "j", "k", "l"])
        logger.debug(f"Test case 3 - node 'b' is BF criminal\n{printTreeString(test2Tree)}")
        criminal = test2Tree.getRoot().getLeft()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'right')

        test2Tree.rightRotation(criminal)

        # Visual check
        logger.debug(f"Test case 3 - {afterRightRotationMsg}:\n{printTreeString(test2Tree)}")
        # Pointers check
        self.rightRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.rightRotationFieldsCheck(nodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(test2Tree, createTreeFromList(
            ["a", "d", "c", "g", "b", "e", "f", None, None, "h", None, "i", "j", "k", "l"])))

    def rightRotationFieldsCheck(self, nodesToCheck):
        self.assertEqual(nodesToCheck["criminalOrigSize"], nodesToCheck["criminalLeftSon"].getSize())
        self.assertEqual(2, nodesToCheck["criminalOrigBF"])
        self.assertEqual(
            max(nodesToCheck["criminal"].getLeft().getHeight(), nodesToCheck["criminal"].getRight().getHeight()) + 1,
            nodesToCheck["criminal"].getHeight())
        self.assertEqual(max(nodesToCheck["criminalLeftSon"].getLeft().getHeight(),
                             nodesToCheck["criminalLeftSon"].getRight().getHeight()) + 1,
                         nodesToCheck["criminalLeftSon"].getHeight())
        self.assertEqual(
            nodesToCheck["criminalRightSon"].getSize() + nodesToCheck["criminalLeftSonRightSon"].getSize() + 1,
            nodesToCheck["criminal"].getSize())
        self.assertTrue(abs(nodesToCheck["criminalLeftSon"].getBalanceFactor()) < 2)

    def leftRotationFieldsCheck(self, nodesToCheck):
        self.assertEqual(nodesToCheck["criminalOrigSize"], nodesToCheck["criminalRightSon"].getSize())
        self.assertEqual(-2, nodesToCheck["criminalOrigBF"])
        self.assertEqual(
            max(nodesToCheck["criminal"].getLeft().getHeight(), nodesToCheck["criminal"].getRight().getHeight()) + 1,
            nodesToCheck["criminal"].getHeight())
        self.assertEqual(max(nodesToCheck["criminalRightSon"].getLeft().getHeight(),
                             nodesToCheck["criminalRightSon"].getRight().getHeight()) + 1,
                         nodesToCheck["criminalRightSon"].getHeight())
        self.assertEqual(
            nodesToCheck["criminalLeftSon"].getSize() + nodesToCheck["criminalRightSonLeftSon"].getSize() + 1,
            nodesToCheck["criminal"].getSize())
        self.assertTrue(abs(nodesToCheck["criminalRightSon"].getBalanceFactor()) < 2)

    def leftThenRightRotationFieldsCheck(self, nodesToCheck):
        self.assertEqual(nodesToCheck["criminalOrigSize"], nodesToCheck["criminalLeftSonRightSon"].getSize())
        self.assertEqual(2, nodesToCheck["criminalOrigBF"])
        self.assertEqual(max(nodesToCheck["criminal"].getLeft().getHeight(),
                             nodesToCheck["criminal"].getRight().getHeight()) + 1,
                         nodesToCheck["criminal"].getHeight())
        self.assertEqual(nodesToCheck["criminalLeftSonRightSon"].getLeft().getSize() + nodesToCheck[
            "criminalLeftSonRightSon"].getRight().getSize() + 1, nodesToCheck["criminalLeftSonRightSon"].getSize())
        self.assertEqual(max(nodesToCheck["criminalLeftSon"].getLeft().getHeight(),
                             nodesToCheck["criminalLeftSon"].getRight().getHeight()) + 1,
                         nodesToCheck["criminalLeftSon"].getHeight())
        self.assertEqual(nodesToCheck["criminalLeftSon"].getLeft().getSize() + nodesToCheck[
            "criminalLeftSon"].getRight().getSize() + 1, nodesToCheck["criminalLeftSon"].getSize())
        if nodesToCheck["criminalLeftSonRightSonRightSon"].getLeft() and nodesToCheck[
            "criminalLeftSonRightSonRightSon"].getRight():
            self.assertEqual(max(nodesToCheck["criminalLeftSonRightSonRightSon"].getLeft().getHeight(),
                                 nodesToCheck["criminalLeftSonRightSonRightSon"].getRight().getHeight()) + 1,
                             nodesToCheck["criminalLeftSonRightSonRightSon"].getHeight())
        if nodesToCheck["criminalLeftSonRightSonRightSon"].getLeft() and nodesToCheck[
            "criminalLeftSonRightSonRightSon"].getRight():
            self.assertEqual(nodesToCheck["criminalLeftSonRightSonRightSon"].getLeft().getSize() + nodesToCheck[
                "criminalLeftSonRightSonRightSon"].getRight().getSize() + 1,
                             nodesToCheck["criminalLeftSonRightSonRightSon"].getSize())
        self.assertEqual(max(nodesToCheck["criminalLeftSonRightSon"].getLeft().getHeight(),
                             nodesToCheck["criminalLeftSonRightSon"].getRight().getHeight()) + 1,
                         nodesToCheck["criminalLeftSonRightSon"].getHeight())
        self.assertEqual(nodesToCheck["criminalLeftSonRightSon"].getLeft().getSize() + nodesToCheck[
            "criminalLeftSonRightSon"].getRight().getSize() + 1, nodesToCheck["criminalLeftSonRightSon"].getSize())
        if nodesToCheck["criminalLeftSonRightSonLeftSon"].getLeft() and nodesToCheck[
            "criminalLeftSonRightSonLeftSon"].getRight():
            self.assertEqual(max(nodesToCheck["criminalLeftSonRightSonLeftSon"].getLeft().getHeight(),
                                 nodesToCheck["criminalLeftSonRightSonLeftSon"].getRight().getHeight()) + 1,
                             nodesToCheck["criminalLeftSonRightSonLeftSon"].getHeight())
        if nodesToCheck["criminalLeftSonRightSonLeftSon"].getLeft() and nodesToCheck[
            "criminalLeftSonRightSonLeftSon"].getRight():
            self.assertEqual(nodesToCheck["criminalLeftSonRightSonLeftSon"].getLeft().getSize() + nodesToCheck[
                "criminalLeftSonRightSonLeftSon"].getRight().getSize() + 1,
                             nodesToCheck["criminalLeftSonRightSonLeftSon"].getSize())

    def rightThenLeftRotationFieldsCheck(self, nodesToCheck):
        self.assertEqual(nodesToCheck["criminalOrigSize"], nodesToCheck["criminalRightSonLeftSon"].getSize())
        self.assertEqual(-2, nodesToCheck["criminalOrigBF"])
        self.assertEqual(max(nodesToCheck["criminal"].getLeft().getHeight(),
                             nodesToCheck["criminal"].getRight().getHeight()) + 1,
                         nodesToCheck["criminal"].getHeight())
        self.assertEqual(nodesToCheck["criminalRightSonLeftSon"].getLeft().getSize() + nodesToCheck[
            "criminalRightSonLeftSon"].getRight().getSize() + 1, nodesToCheck["criminalRightSonLeftSon"].getSize())
        self.assertEqual(max(nodesToCheck["criminalRightSon"].getLeft().getHeight(),
                             nodesToCheck["criminalRightSon"].getRight().getHeight()) + 1,
                         nodesToCheck["criminalRightSon"].getHeight())
        self.assertEqual(nodesToCheck["criminalRightSon"].getLeft().getSize() + nodesToCheck[
            "criminalRightSon"].getRight().getSize() + 1, nodesToCheck["criminalRightSon"].getSize())
        if nodesToCheck["criminalRightSonLeftSonLeftSon"].getLeft() and nodesToCheck[
            "criminalRightSonLeftSonLeftSon"].getRight():
            self.assertEqual(max(nodesToCheck["criminalRightSonLeftSonLeftSon"].getLeft().getHeight(),
                                 nodesToCheck["criminalRightSonLeftSonLeftSon"].getRight().getHeight()) + 1,
                             nodesToCheck["criminalRightSonLeftSonLeftSon"].getHeight())
        if nodesToCheck["criminalRightSonLeftSonLeftSon"].getLeft() and nodesToCheck[
            "criminalRightSonLeftSonLeftSon"].getRight():
            self.assertEqual(nodesToCheck["criminalRightSonLeftSonLeftSon"].getLeft().getSize() + nodesToCheck[
                "criminalRightSonLeftSonLeftSon"].getRight().getSize() + 1,
                             nodesToCheck["criminalRightSonLeftSonLeftSon"].getSize())
        self.assertEqual(max(nodesToCheck["criminalRightSonLeftSon"].getLeft().getHeight(),
                             nodesToCheck["criminalRightSonLeftSon"].getRight().getHeight()) + 1,
                         nodesToCheck["criminalRightSonLeftSon"].getHeight())
        self.assertEqual(nodesToCheck["criminalRightSonLeftSon"].getLeft().getSize() + nodesToCheck[
            "criminalRightSonLeftSon"].getRight().getSize() + 1, nodesToCheck["criminalRightSonLeftSon"].getSize())
        if nodesToCheck["criminalRightSonLeftSonRightSon"].getLeft() and nodesToCheck[
            "criminalRightSonLeftSonRightSon"].getRight():
            self.assertEqual(max(nodesToCheck["criminalRightSonLeftSonRightSon"].getLeft().getHeight(),
                                 nodesToCheck["criminalRightSonLeftSonRightSon"].getRight().getHeight()) + 1,
                             nodesToCheck["criminalRightSonLeftSonRightSon"].getHeight())
        if nodesToCheck["criminalRightSonLeftSonRightSon"].getLeft() and nodesToCheck[
            "criminalRightSonLeftSonRightSon"].getRight():
            self.assertEqual(nodesToCheck["criminalRightSonLeftSonRightSon"].getLeft().getSize() + nodesToCheck[
                "criminalRightSonLeftSonRightSon"].getRight().getSize() + 1,
                             nodesToCheck["criminalRightSonLeftSonRightSon"].getSize())

    def rightRotationPointersCheck(self, parentSon, nodesToCheck):
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalLeftSonRightSon"].getParent())
        self.assertEqual(nodesToCheck["criminalLeftSonRightSon"], nodesToCheck["criminal"].getLeft())

        self.assertEqual(nodesToCheck["criminalParent"], nodesToCheck["criminalLeftSon"].getParent())
        if parentSon == 'left':
            self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck['criminalParent'].getLeft())
        elif parentSon == 'right':
            self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck['criminalParent'].getRight())
        else:
            self.assertEqual(None, nodesToCheck["criminalLeftSon"].getParent())

        self.assertEqual(nodesToCheck["criminalLeftSonLeftSon"], nodesToCheck["criminalLeftSon"].getLeft())
        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminalLeftSonLeftSon"].getParent())

        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminal"].getRight())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalRightSon"].getParent())

        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminal"].getParent())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalLeftSon"].getRight())

    def leftRotationPointersCheck(self, parentSon, nodesToCheck):
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalRightSonLeftSon"].getParent())
        self.assertEqual(nodesToCheck["criminalRightSonLeftSon"], nodesToCheck["criminal"].getRight())

        self.assertEqual(nodesToCheck["criminalParent"], nodesToCheck["criminalRightSon"].getParent())
        if parentSon == 'left':
            self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck['criminalParent'].getLeft())
        elif parentSon == 'right':
            self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck['criminalParent'].getRight())
        else:
            self.assertEqual(None, nodesToCheck["criminalRightSon"].getParent())

        self.assertEqual(nodesToCheck["criminalRightSonRightSon"], nodesToCheck["criminalRightSon"].getRight())
        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminalRightSonRightSon"].getParent())

        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminal"].getLeft())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalLeftSon"].getParent())

        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminal"].getParent())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalRightSon"].getLeft())

    def leftThenRightRotationPointersCheck(self, parentSon, nodesToCheck):
        self.assertEqual(nodesToCheck["criminalLeftSonRightSon"], nodesToCheck["criminal"].getParent())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalLeftSonRightSon"].getRight())

        self.assertEqual(nodesToCheck["criminalLeftSonRightSonRightSon"], nodesToCheck["criminal"].getLeft())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalLeftSonRightSonRightSon"].getParent())

        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalRightSon"].getParent())
        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminal"].getRight())

        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminalLeftSonLeftSon"].getParent())
        self.assertEqual(nodesToCheck["criminalLeftSonLeftSon"], nodesToCheck["criminalLeftSon"].getLeft())

        self.assertEqual(nodesToCheck["criminalParent"], nodesToCheck["criminalLeftSonRightSon"].getParent())
        if parentSon == 'left':
            self.assertEqual(nodesToCheck["criminalLeftSonRightSon"], nodesToCheck["criminalParent"].getLeft())
        elif parentSon == 'right':
            self.assertEqual(nodesToCheck["criminalLeftSonRightSon"], nodesToCheck["criminalParent"].getRight())
        else:
            self.assertEqual(None, nodesToCheck["criminalLeftSonRightSon"].getParent())

        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminalLeftSonRightSonLeftSon"].getParent())
        self.assertEqual(nodesToCheck["criminalLeftSonRightSonLeftSon"], nodesToCheck["criminalLeftSon"].getRight())

        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminalLeftSonRightSon"].getLeft())
        self.assertEqual(nodesToCheck["criminalLeftSonRightSon"], nodesToCheck["criminalLeftSon"].getParent())

    def rightThenLeftRotationPointersCheck(self, parentSon, nodesToCheck):
        self.assertEqual(nodesToCheck["criminalRightSonLeftSon"], nodesToCheck["criminal"].getParent())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalRightSonLeftSon"].getLeft())

        self.assertEqual(nodesToCheck["criminalRightSonLeftSonLeftSon"], nodesToCheck["criminal"].getRight())
        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalRightSonLeftSonLeftSon"].getParent())

        self.assertEqual(nodesToCheck["criminal"], nodesToCheck["criminalLeftSon"].getParent())
        self.assertEqual(nodesToCheck["criminalLeftSon"], nodesToCheck["criminal"].getLeft())

        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminalRightSonRightSon"].getParent())
        self.assertEqual(nodesToCheck["criminalRightSonRightSon"], nodesToCheck["criminalRightSon"].getRight())

        self.assertEqual(nodesToCheck["criminalParent"], nodesToCheck["criminalRightSonLeftSon"].getParent())
        if parentSon == 'left':
            self.assertEqual(nodesToCheck["criminalRightSonLeftSon"], nodesToCheck["criminalParent"].getLeft())
        elif parentSon == 'right':
            self.assertEqual(nodesToCheck["criminalRightSonLeftSon"], nodesToCheck["criminalParent"].getRight())
        else:
            self.assertEqual(None, nodesToCheck["criminalRightSonLeftSon"].getParent())

        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminalRightSonLeftSonRightSon"].getParent())
        self.assertEqual(nodesToCheck["criminalRightSonLeftSonRightSon"], nodesToCheck["criminalRightSon"].getLeft())

        self.assertEqual(nodesToCheck["criminalRightSon"], nodesToCheck["criminalRightSonLeftSon"].getRight())
        self.assertEqual(nodesToCheck["criminalRightSonLeftSon"], nodesToCheck["criminalRightSon"].getParent())

    def test_leftRotation(self):
        afterLeftRotationMsg = "after left rotation"

        # Test case 1: left rotation when the root is the criminal
        rootCriminalTree = createTreeFromList(["a", None, "b", None, None, None, "c"])
        logger.debug(f"Test case 1 - root 'a' is BF criminal\n{printTreeString(rootCriminalTree)}")
        criminal = rootCriminalTree.getRoot()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'left')

        rootCriminalTree.leftRotation(criminal)

        # Visual check
        logger.debug(f"Test case 1 - {afterLeftRotationMsg}:\n{printTreeString(rootCriminalTree)}")
        # Pointers check
        self.leftRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.leftRotationFieldsCheck(nodesToCheck)
        # Undependent check
        expectedTree = createTreeFromList(["b", "a", "c"])
        self.assertTrue(treesEqual(rootCriminalTree, expectedTree))

        # Test case 2: left rotation when some node is the criminal (BF of criminal.right == -1)
        test2Tree = createTreeFromList(["a", "b", "c", "d", "e", None, "f", "g", "h", "i", "j", "k", None, None, "k"])
        logger.debug(f"Test case 2 - node 'c' is BF criminal\n{printTreeString(test2Tree)}")
        criminal = test2Tree.getRoot().getRight()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'left')

        test2Tree.leftRotation(criminal)

        # Visual check
        logger.debug(f"Test case 2 - {afterLeftRotationMsg}:\n{printTreeString(test2Tree)}")
        # Pointers check
        self.leftRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.leftRotationFieldsCheck(nodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(test2Tree, createTreeFromList(
            ["a", "b", "f", "d", "e", "c", "k", "g", "h", "i", "j", None, None, None, None])))

        # Test case 3: left rotation when some node is the criminal (BF of criminal.right == 0)
        test3Tree = createTreeFromList(["a", "b", "c", "d", "e", None, "f", "g", "h", "i", "j", None, None, "k", "l"])
        logger.debug(f"Test case 3 - node 'b' is BF criminal\n{printTreeString(test3Tree)}")
        criminal = test3Tree.getRoot().getRight()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'left')

        test3Tree.leftRotation(criminal)

        # Visual check
        logger.debug(f"Test case 3 - {afterLeftRotationMsg}:\n{printTreeString(test3Tree)}")
        # Pointers check
        self.leftRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.leftRotationFieldsCheck(nodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(test3Tree, createTreeFromList(
            ["a", "b", "f", "d", "e", "c", "l", "g", "h", "i", "j", None, "k", None, None])))

    @staticmethod
    def getAboutToChangeNodes(criminal, rotation):
        if rotation == 'right':
            nodesToCheck = {
                "criminal": criminal,
                "criminalOrigSize": criminal.getSize(),
                "criminalOrigBF": criminal.getBalanceFactor(),
                "criminalParent": criminal.getParent(),
                "criminalLeftSon": criminal.getLeft(),
                "criminalRightSon": criminal.getRight(),
                "criminalLeftSonLeftSon": criminal.getLeft().getLeft(),
                "criminalLeftSonRightSon": criminal.getLeft().getRight()
            }
        elif rotation == 'left':
            nodesToCheck = {
                "criminal": criminal,
                "criminalOrigSize": criminal.getSize(),
                "criminalOrigBF": criminal.getBalanceFactor(),
                "criminalParent": criminal.getParent(),
                "criminalLeftSon": criminal.getLeft(),
                "criminalRightSon": criminal.getRight(),
                "criminalRightSonLeftSon": criminal.getRight().getLeft(),
                "criminalRightSonRightSon": criminal.getRight().getRight()
            }
        elif rotation == "leftThenRight":
            nodesToCheck = {
                "criminal": criminal,
                "criminalOrigSize": criminal.getSize(),
                "criminalOrigBF": criminal.getBalanceFactor(),
                "criminalParent": criminal.getParent(),
                "criminalLeftSon": criminal.getLeft(),
                "criminalRightSon": criminal.getRight(),
                "criminalLeftSonLeftSon": criminal.getLeft().getLeft(),
                "criminalLeftSonRightSon": criminal.getLeft().getRight(),
                "criminalLeftSonRightSonLeftSon": criminal.getLeft().getRight().getLeft(),
                "criminalLeftSonRightSonRightSon": criminal.getLeft().getRight().getRight(),
            }
        elif rotation == 'rightThenLeft':
            nodesToCheck = {
                "criminal": criminal,
                "criminalOrigSize": criminal.getSize(),
                "criminalOrigBF": criminal.getBalanceFactor(),
                "criminalParent": criminal.getParent(),
                "criminalLeftSon": criminal.getLeft(),
                "criminalRightSon": criminal.getRight(),
                "criminalRightSonLeftSon": criminal.getRight().getLeft(),
                "criminalRightSonRightSon": criminal.getRight().getRight(),
                "criminalRightSonLeftSonLeftSon": criminal.getRight().getLeft().getLeft(),
                "criminalRightSonLeftSonRightSon": criminal.getRight().getLeft().getRight(),
            }
        return nodesToCheck

    @staticmethod
    def determineParentSon(node):
        if not node.getParent():
            return None
        elif node.getParent().getLeft() == node:
            return "left"
        elif node.getParent().getRight() == node:
            return "right"

    def test_leftThenRightRotation(self):
        afterLeftThenRightRotationMsg = "after left then right rotation"

        # Test case 1: left then right rotation when the root is the criminal
        rootCriminalTree = createTreeFromList(["a", "b", None, None, "c", None, None])
        logger.debug(f"Test case 1 - root 'a' is BF criminal\n{printTreeString(rootCriminalTree)}")
        criminal = rootCriminalTree.getRoot()
        parentSon = self.determineParentSon(criminal)
        leftThenRightRotationNodesToCheck = self.getAboutToChangeNodes(criminal, 'leftThenRight')

        rootCriminalTree.leftThenRightRotation(criminal)

        # Final Visual Check
        logger.debug(f"Test case 1 - {afterLeftThenRightRotationMsg}:\n{printTreeString(rootCriminalTree)}")
        # Final Pointers Check
        self.leftThenRightRotationPointersCheck(parentSon, leftThenRightRotationNodesToCheck)
        # Final Fields Check
        self.leftThenRightRotationFieldsCheck(leftThenRightRotationNodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(rootCriminalTree, createTreeFromList(["c", "b", "a"])))

        # Test case 2: left then right rotation when some node is the criminal
        test2Tree = createTreeFromList(["a", "b", "c", "d", None, "e", "f", None, "g", None, None, "i", "j", "k", "l"])
        logger.debug(f"Test case 2 - node 'b' is BF criminal\n{printTreeString(test2Tree)}")
        criminal = test2Tree.getRoot().getLeft()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'leftThenRight')

        test2Tree.leftThenRightRotation(criminal)

        # Visual check
        logger.debug(f"Test case 2 - {afterLeftThenRightRotationMsg}:\n{printTreeString(test2Tree)}")
        # Pointers check
        self.leftThenRightRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.leftThenRightRotationFieldsCheck(nodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(test2Tree, createTreeFromList(
            ["a", "g", "c", "d", "b", "e", "f", None, None, None, None, "i", "j", "k", "l"])))

    def test_rightThenLeftRotation(self):
        afterRightThenLeftRotationMsg = "after right then left rotation"

        # Test case 1: left then right rotation when the root is the criminal
        rootCriminalTree = createTreeFromList(["a", None, "c", None, None, "b", None])
        logger.debug(f"Test case 1 - root 'a' is BF criminal\n{printTreeString(rootCriminalTree)}")
        criminal = rootCriminalTree.getRoot()
        parentSon = self.determineParentSon(criminal)
        rightThenLeftRotationNodesToCheck = self.getAboutToChangeNodes(criminal, 'rightThenLeft')

        rootCriminalTree.rightThenLeftRotation(criminal)

        # Final Visual Check
        logger.debug(f"Test case 1 - {afterRightThenLeftRotationMsg}:\n{printTreeString(rootCriminalTree)}")
        # Final Pointers Check
        self.rightThenLeftRotationPointersCheck(parentSon, rightThenLeftRotationNodesToCheck)
        # Final Fields Check
        self.rightThenLeftRotationFieldsCheck(rightThenLeftRotationNodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(rootCriminalTree, createTreeFromList(["b", "a", "c"])))

        # Test case 2: left then right rotation when some node is the criminal
        test2Tree = createTreeFromList(["a", "b", "c", "d", "e", None, "f", "g", "i", "j", "k", None, None, "l", None])
        logger.debug(f"Test case 2 - node 'c' is BF criminal\n{printTreeString(test2Tree)}")
        criminal = test2Tree.getRoot().getRight()
        parentSon = self.determineParentSon(criminal)
        nodesToCheck = self.getAboutToChangeNodes(criminal, 'rightThenLeft')

        test2Tree.rightThenLeftRotation(criminal)

        # Visual check
        logger.debug(f"Test case 2 - {afterRightThenLeftRotationMsg}:\n{printTreeString(test2Tree)}")
        # Pointers check
        self.rightThenLeftRotationPointersCheck(parentSon, nodesToCheck)
        # Fields check
        self.rightThenLeftRotationFieldsCheck(nodesToCheck)
        # Undependent check
        self.assertTrue(treesEqual(test2Tree, createTreeFromList(
            ["a", "b", "l", "d", "e", "c", "f", "g", "i", "j", "k", None, None, None, None])))

    @unittest.skip("Waiting for insert & join implementation")
    def test_concat(self):
        # Case 1: concat 2 empty trees
        case1tree1 = createTreeFromList([])
        case1tree2 = createTreeFromList([])
        case1tree1ltr = case1tree1.listToArray()
        case1tree2ltr = case1tree2.listToArray()
        logger.debug("concatDebug - case 1:")
        logger.debug("tree1 as list:", case1tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case1tree1))
        logger.debug("tree2 as list:", case1tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case1tree2))
        absDiffHeight = case1tree1.concat(case1tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 0
        logger.debug("new concatinated list:", case1tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case1tree1))
        self.assertEqual(0, absDiffHeight)
        # Undependent check
        self.assertEqual(case1tree1ltr + case1tree2ltr, case1tree1.listToArray())

        # Case 2: self is empty tree, other is not
        case2tree1 = createTreeFromList([])
        case2tree2 = createTreeFromList(["a", "b", None])
        case2tree1ltr = case2tree1.listToArray()
        case2tree2ltr = case2tree2.listToArray()
        logger.debug("concatDebug - case 2:")
        logger.debug("tree1 as list:", case2tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case2tree1))
        logger.debug("tree2 as list:", case2tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case2tree2))
        absDiffHeight = case2tree1.concat(case2tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 2
        logger.debug("new concatinated list:", case2tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case2tree1))
        self.assertEqual(2, absDiffHeight)
        # Undependent check
        self.assertEqual(case2tree1ltr + case2tree2ltr, case2tree1.listToArray())

        # Case 3: self is not empty, other is empty
        case3tree1 = createTreeFromList(["a", "b", None])
        case3tree2 = createTreeFromList([])
        case3tree1ltr = case3tree1.listToArray()
        case3tree2ltr = case3tree2.listToArray()
        logger.debug("concatDebug - case 3:")
        logger.debug("tree1 as list:", case3tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case3tree1))
        logger.debug("tree2 as list:", case3tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case3tree2))
        absDiffHeight = case3tree1.concat(case3tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 2
        logger.debug("new concatinated list:", case3tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case3tree1))
        self.assertEqual(2, absDiffHeight)
        # Undependent check
        self.assertEqual(case3tree1ltr + case3tree2ltr, case3tree1.listToArray())

        # Case 4: self has only a root, other has only a root TODO: check after evia's insert
        case4tree1 = createTreeFromList(["a"])
        case4tree2 = createTreeFromList(["b"])
        case4tree1ltr = case4tree1.listToArray()
        case4tree2ltr = case4tree2.listToArray()
        logger.debug("concatDebug - case 4:")
        logger.debug("tree1 as list:", case4tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case4tree1))
        logger.debug("tree2 as list:", case4tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case4tree2))
        absDiffHeight = case4tree1.concat(case4tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 0
        logger.debug("new concatinated list:", case4tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case4tree1))
        self.assertEqual(0, absDiffHeight)
        # Undependent check
        self.assertEqual(case4tree1ltr + case4tree2ltr, case4tree1.listToArray())

        # Case 5: self has only a root, other is a larger tree TODO: check after evia's insert
        case5tree1 = createTreeFromList(["a"])
        case5tree2 = createTreeFromList(["b", "c", "d"])
        case5tree1ltr = case5tree1.listToArray()
        case5tree2ltr = case5tree2.listToArray()
        logger.debug("concatDebug - case 5:")
        logger.debug("tree1 as list:", case5tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case5tree1))
        logger.debug("tree2 as list:", case5tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case5tree2))
        absDiffHeight = case5tree1.concat(case5tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 1
        logger.debug("new concatinated list:", case5tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case5tree1))
        self.assertEqual(1, absDiffHeight)
        # Undependent check
        self.assertEqual(case5tree1ltr + case5tree2ltr, case5tree1.listToArray())

        # Case 6: self's size is larger than 1 and other is a larger tree TODO: check after evia's join
        case6tree1 = createTreeFromList(["a", "b", "c"])
        case6tree2 = createTreeFromList(["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
        case6tree1ltr = case6tree1.listToArray()
        case6tree2ltr = case6tree2.listToArray()
        logger.debug("concatDebug - case 6:")
        logger.debug("tree1 as list:", case6tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case6tree1))
        logger.debug("tree2 as list:", case6tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case6tree2))
        absDiffHeight = case6tree1.concat(case6tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 2
        logger.debug("new concatinated list:", case6tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case6tree1))
        self.assertEqual(2, absDiffHeight)
        # Undependent check
        self.assertEqual(case6tree1ltr + case6tree2ltr, case6tree1.listToArray())

        # Case 7: self's size is larger than 1 and other is a smaller tree TODO: check after evia's join
        case7tree1 = createTreeFromList(["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
        case7tree2 = createTreeFromList(["a", "b", "c"])
        case7tree1ltr = case7tree1.listToArray()
        case7tree2ltr = case7tree2.listToArray()
        logger.debug("concatDebug - case 7:")
        logger.debug("tree1 as list:", case7tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case7tree1))
        logger.debug("tree2 as list:", case7tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case7tree2))
        absDiffHeight = case7tree1.concat(case7tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 2
        logger.debug("new concatinated list:", case7tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case7tree1))
        self.assertEqual(2, absDiffHeight)
        # Undependent check
        self.assertEqual(case7tree1ltr + case7tree2ltr, case7tree1.listToArray())

        # Case 8: self's size is larger than 1 and other has only a root TODO: check after evia's join
        case8tree1 = createTreeFromList(["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
        case8tree2 = createTreeFromList(["a"])
        case8tree1ltr = case8tree1.listToArray()
        case8tree2ltr = case8tree2.listToArray()
        logger.debug("concatDebug - case 8:")
        logger.debug("tree1 as list:", case8tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case8tree1))
        logger.debug("tree2 as list:", case8tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case8tree2))
        absDiffHeight = case8tree1.concat(case8tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 3
        logger.debug("new concatinated list:", case8tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case8tree1))
        self.assertEqual(3, absDiffHeight)
        # Undependent check
        self.assertEqual(case8tree1ltr + case8tree2ltr, case8tree1.listToArray())

        # Case 9: self's size is larger than 1 and other is equal in size to self TODO: check after evia's join
        case9tree1 = createTreeFromList(["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"])
        case9tree2 = createTreeFromList(
            ["d'", "e'", "f'", "g'", "h'", "i'", "j'", "k'", "l'", "m'", "n'", "o'", "p'", "q'", "r'"])
        case9tree1ltr = case9tree1.listToArray()
        case9tree2ltr = case9tree2.listToArray()
        logger.debug("concatDebug - case 9:")
        logger.debug("tree1 as list:", case9tree1.listToArray())
        logger.debug("tree1 as tree:\n" + printTreeString(case9tree1))
        logger.debug("tree2 as list:", case9tree2.listToArray())
        logger.debug("tree2 as tree:\n" + printTreeString(case9tree2))
        absDiffHeight = case9tree1.concat(case9tree2)
        logger.debug("absDiffHeight:", absDiffHeight)  # should be 0
        logger.debug("new concatinated list:", case9tree1.listToArray())
        logger.debug("new list as a tree:\n" + printTreeString(case9tree1))
        self.assertEqual(0, absDiffHeight)
        # Undependent check
        self.assertEqual(case9tree1ltr + case9tree2ltr, case9tree1.listToArray())

    def test_insert(self):
        # case 1: tree is empty
        case1tree = createTreeFromList([])
        logger.debug("insertDebug - case 1:")
        logger.debug("tree before insert:\n" + printTreeString(case1tree))
        case1BalanceOps = case1tree.insert(0, "A")
        logger.debug("tree after insertion:\n" + printTreeString(case1tree))
        logger.debug(f"case1 balanceOps: {case1BalanceOps}")  # should be 1
        self.assertEqual(0, case1BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case1tree, createTreeFromList(["A"])))
        self.assertTrue(case1tree.getRoot(),case1tree.get_First())
        self.assertTrue(case1tree.get_First(), case1tree.get_Last())

        # case 2: balanced tree, insert First
        case2tree = createTreeFromList(["c", "b", "d"])
        logger.debug("tree before insert:\n" + printTreeString(case2tree))
        case2BalanceOps = case2tree.insert(0, "a")
        logger.debug("tree after insertion:\n" + printTreeString(case2tree))
        logger.debug(f"case2 balanceOps: {case2BalanceOps}")  # should be 2
        self.assertEqual(2, case2BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case2tree, createTreeFromList(["c", "b", "d", "a", None, None, None])))

        # case 3: balanced tree, insert Last
        case3tree = createTreeFromList(["c", "b", "d"])
        logger.debug("tree before insert:\n" + printTreeString(case3tree))
        case3BalanceOps = case3tree.insert(3, "e")
        logger.debug("tree after insertion:\n" + printTreeString(case3tree))
        logger.debug(f"case3 balanceOps: {case3BalanceOps}")  # should be 2
        self.assertEqual(2, case3BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case3tree, createTreeFromList(["c", "b", "d", None, None, None, "e"])))

        # case 4: tree has only root, insert as leftson
        case4tree = createTreeFromList(["b"])
        logger.debug("tree before insert:\n" + printTreeString(case4tree))
        case4BalanceOps = case4tree.insert(0, "a")
        logger.debug("tree after insertion:\n" + printTreeString(case4tree))
        logger.debug(f"case4 balanceOps: {case4BalanceOps}")  # should be 1
        self.assertEqual(1, case4BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case4tree, createTreeFromList(["b", "a", None])))

        # case 5: tree has only root, insert as rightson
        case5tree = createTreeFromList(["a"])
        logger.debug("tree before insert:\n" + printTreeString(case5tree))
        case5BalanceOps = case5tree.insert(1, "b")
        logger.debug("tree after insertion:\n" + printTreeString(case5tree))
        logger.debug(f"case5 balanceOps: {case5BalanceOps}")  # should be 1
        self.assertEqual(1, case5BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case5tree, createTreeFromList(["a", None, "b"])))

        # case 6: insertion that causes right rotation
        case6tree = createTreeFromList(["b", "a", "c", None, None, None, "d"])
        logger.debug("tree before insert:\n" + printTreeString(case6tree))
        case6BalanceOps = case6tree.insert(4, "e")
        logger.debug("tree after insertion:\n" + printTreeString(case6tree))
        logger.debug(f"case6 balanceOps: {case6BalanceOps}")  # should be 2
        self.assertEqual(2, case6BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case6tree, createTreeFromList(["b", "a", "d", None, None, "c", "e"])))

        # case 7: insertion that causes right then left rotation
        case7tree = createTreeFromList(["b", "a", "c", None, None, None, "e"])
        logger.debug("tree before insert:\n" + printTreeString(case7tree))
        case7BalanceOps = case7tree.insert(3, "d")
        logger.debug("tree after insertion:\n" + printTreeString(case7tree))
        logger.debug(f"case7 balanceOps: {case7BalanceOps}")  # should be 3
        self.assertEqual(4, case7BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case7tree, createTreeFromList(["b", "a", "d", None, None, "c", "e"])))

        #case 8: first tree from lecture, slide 50, insert 18: https://visualgo.net/en/bst?mode=AVL&create=12,8,15,6,10,11,14,13,24,20,19,29
        case8tree = createTreeFromList([
            "12",
            "8", "15",
            "6", "10", "14", "24",
            None, None, None, "11", "13", None, "20", "29",
            None, None, None, None, None, None, None, None, None, None, None, None, "19", None, None, None
        ])
        logger.debug("tree before insert:\n" + printTreeString(case8tree))
        logger.debug(case8tree.search("19"))
        case8BalanceOps = case8tree.insert(8, "18")
        logger.debug("tree after insertion:\n" + printTreeString(case8tree))
        logger.debug(f"case8 balanceOps: {case8BalanceOps}")  # should be 2
        self.assertEqual(2, case8BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case8tree, createTreeFromList([
            "12",
            "8", "15",
            "6", "10", "14", "24",
            None, None, None, "11", "13", None, "19", "29",
            None, None, None, None, None, None, None, None, None, None, None, None, "18", "20", None, None
        ])))

        #case 9: second tree from lecture, slide 63, insert 5: https://visualgo.net/en/bst?mode=AVL&create=15,10,22,4,11,20,24,2,7,12,18,1,6,8
        case9tree = createTreeFromList([
            "15",
            "10", "22",
            "4", "11", "20", "24",
            "2", "7", None, "12", "18", None, None, None,
            "1", None, "6", "8", None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("tree before insert:\n" + printTreeString(case9tree))
        case9BalanceOps = case9tree.insert(3, "5")
        logger.debug("tree after insertion:\n" + printTreeString(case9tree))
        logger.debug(f"case9 balanceOps: {case9BalanceOps}")  # should be 2
        self.assertEqual(5, case9BalanceOps)
        # Undependent check
        expected = createTreeFromList([
            "15",
            "7", "22",
            "4", "10", "20", "24",
            "2", "6", "8", "11", "18", None, None, None,
            "1", None, "5", None, None, None, None, "12", None, None, None, None, None, None, None, None
        ])
        self.assertTrue(treesEqual(case9tree, expected))

        #dvir & or tester for insert
        tree1 = AVLTreeList()
        tree2 = AVLTreeList()
        tree3 = AVLTreeList()
        tree4 = AVLTreeList()
        tree1.insert(0, "2")
        tree1.insert(0, "1")
        tree1.insert(0, "0")
        tree2.insert(0, "0")
        tree2.insert(1, "1")
        tree2.insert(2, "2")
        tree3.insert(0, "0")
        tree3.insert(1, "2")
        tree3.insert(1, "1")
        tree4.insert(0, "2")
        tree4.insert(0, "0")
        tree4.insert(1, "1")

        root1 = tree1.getRoot()
        root2 = tree2.getRoot()
        root3 = tree3.getRoot()
        root4 = tree4.getRoot()
        self.assertEqual(True, root1.getValue() == root2.getValue() and root3.getValue() == root4.getValue())
        self.assertEqual(True, root1.getValue() == root3.getValue() and root2.getValue() == root4.getValue())
        self.assertEqual(True,
                         root1.left.getValue() == root2.left.getValue() and root3.left.getValue() == root4.left.getValue())
        self.assertEqual(True,
                         root1.left.getValue() == root3.left.getValue() and root2.left.getValue() == root4.left.getValue())
        self.assertEqual(True,
                         root1.right.getValue() == root2.right.getValue() and root3.right.getValue() == root4.right.getValue())
        self.assertEqual(True,
                         root1.right.getValue() == root3.right.getValue() and root2.right.getValue() == root4.right.getValue())
        self.assertEqual(True, tree1.first() == tree2.first() and tree3.first() == tree4.first())
        self.assertEqual(True, tree1.first() == tree3.first() and tree2.first() == tree4.first())
        self.assertEqual(True, tree1.last() == tree2.last() and tree3.last() == tree4.last())
        self.assertEqual(True, tree1.last() == tree3.last() and tree2.last() == tree4.last())
        self.assertEqual(True,
                         tree1.listToArray() == tree2.listToArray() and tree3.listToArray() == tree4.listToArray())
        self.assertEqual(True,
                         tree1.listToArray() == tree3.listToArray() and tree2.listToArray() == tree4.listToArray())
        self.assertEqual(True, tree1.length() == tree2.length() and tree3.length() == tree4.length())
        self.assertEqual(True, tree1.length() == tree3.length() and tree2.length() == tree4.length())
        a = root4.left.getHeight()
        c = root3.left.getHeight()

        self.assertEqual(True, root1.getHeight() == root2.getHeight() and root3.getHeight() == root4.getHeight())
        self.assertEqual(True, root1.getHeight() == root3.getHeight() and root2.getHeight() == root4.getHeight())
        tree1 = AVLTreeList()
        self.assertEqual(True, tree1.insert(0, None) == 0)
        self.assertEqual(True, tree1.insert(1, None) == 1)
        self.assertEqual(True, tree1.insert(0, None) == 0)
        self.assertEqual(True, tree1.insert(0, None) == 2)
        self.assertEqual(True, tree1.insert(2, None) == 0)
        self.assertEqual(True, tree1.insert(0, None) == 3)
        self.assertEqual(True, tree1.insert(0, None) == 2)
        self.assertEqual(True, tree1.listToArray() == [None for i in range(7)])
        self.assertEqual(True, tree1.insert(4, None) == 3)
        self.assertEqual(True, tree1.insert(5, None) == 3)
        self.assertEqual(True, tree1.length() == 9)
        self.assertEqual(True, tree1.getRoot().left.getSize() == 3)
        self.assertEqual(True, tree1.getRoot().right.getSize() == 5)
        self.assertEqual(True, tree1.getRoot().left.getHeight() == 1)
        self.assertEqual(True, tree1.getRoot().getHeight() == 3)
        self.assertEqual(True, tree1.getRoot().right.getHeight() == 2)


    def test_createTreeFromListInsert(self):
        expected = createTreeFromList([
            "10",
            "5", "18",
            "2", "7", "12", "22",
            "1", "4", "6", "8", "11", "15", "20", "24"
        ])
        tree = createTreeFromListInsert(["1","2","4","5","6","7","8","10", "11", "12", "15", "18", "20", "22", "24"])
        logger.debug("Actual: \n"+ printTreeString(tree))
        self.assertTrue(treesEqual(expected,tree))


    def test_join(self):
        #case1 2 trees with equal height
        T1 = createTreeFromList(["1"])
        T2 = createTreeFromList(["3"])
        node_x = AVLNode("2")
        node_x.setHeight(0)
        node_x.setSize(1)
        T = AVLTreeList.join(T1, node_x, T2)[0]
        num = AVLTreeList.join(T1, node_x, T2)[1]
        logger.debug("Joined tree: \n"+printTreeString(T))
        self.assertTrue(treesEqual(T, createTreeFromList(["2", "1", "3"])))
        self.assertEqual(num, 1)

        #case2,  left subtree height is bigger than the right one
        T3 = createTreeFromList(["2", "1", "3"])
        T4 = createTreeFromList(["8", "6", "10", "5", "7", "9", "11"])
        logger.debug("T1: \n"+printTreeString(T3))
        logger.debug("T2: \n" + printTreeString(T4))
        node_x = AVLNode("4")
        node_x.setHeight(0)
        node_x.setSize(1)
        T = AVLTreeList.join(T3, node_x,T4)[0]
        logger.debug("Joined tree: \n"+printTreeString(T))
        self.assertTrue(treesEqual(T, createTreeFromList(["8", "4", "10", "2", "6", "9", "11", "1", "3", "5", "7", None, None, None, None])))

        #case3, right subtree height is bigger than the left one
        T5 = createTreeFromListInsert(["1", "2", "3", "4", "5", "6", "7", "8","9","10","11","12","13","14","15"])
        T6 = createTreeFromListInsert(["17","18","19"])
        logger.debug("T5: \n"+printTreeString(T5))
        logger.debug("T6: \n"+printTreeString(T6))
        node_x = AVLNode("16")
        node_x.setHeight(0)
        node_x.setSize(1)
        T = AVLTreeList.join(T5, node_x, T6)[0]
        logger.debug("Joined tree: \n"+printTreeString(T))
        expected = createTreeFromList(
            ["8", "4", "12", "2", "6", "10", "16", "1", "3", "5", "7", "9", "11", "14", "18"])
        logger.debug(expected.search("14"))
        expected.insert(12,"13")
        expected.insert(14,"15")
        expected.insert(16, "17")
        expected.insert(18, "19")
        self.assertTrue(treesEqual(T, expected))

    def test_delete(self):
        # Case 1: tree has only a root - delete root
        case1tree = createTreeFromList(["a"])
        logger.debug("deleteDebug - case 1:")
        logger.debug("tree before delete:\n" + printTreeString(case1tree))
        case1BalanceOps = case1tree.delete(0)
        logger.debug("tree after delete:\n" + printTreeString(case1tree))
        logger.debug(f"case1 balanceOps: {case1BalanceOps}")  # should be 0
        self.assertEqual(0, case1BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case1tree, createTreeFromList([])))

        # Case 2: deleting a leaf
        case2tree = createTreeFromList(["a", "b", "c", "d", "e", "f", "g"])
        logger.debug("deleteDebug - case 2:")
        logger.debug("tree before delete:\n" + printTreeString(case2tree))
        case2BalanceOps = case2tree.delete(2)
        logger.debug("tree after delete:\n" + printTreeString(case2tree))
        logger.debug(f"case2 balanceOps: {case2BalanceOps}")  # should be 0
        self.assertEqual(0, case2BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case2tree, createTreeFromList(["a", "b", "c", "d", None, "f", "g"])))

        # Case 3: deleting a leaf that was the minimum
        case3tree = createTreeFromList(["a", "b", "c", "d", "e", "f", "g"])
        logger.debug("deleteDebug - case 3:")
        logger.debug("tree before delete:\n" + printTreeString(case3tree))
        logger.debug("minimum before delete:\n" + case3tree.get_First().getValue())  # should be d
        case3BalanceOps = case3tree.delete(0)
        logger.debug("tree after delete:\n" + printTreeString(case3tree))
        logger.debug(f"case3 balanceOps: {case3BalanceOps}")  # should be 0
        logger.debug("minimum after delete:\n" + case3tree.get_First().getValue())  # should be b
        self.assertEqual(0, case3BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case3tree, createTreeFromList(["a", "b", "c", None, "e", "f", "g"])))

        # Case 4: deleting a leaf that was the maximum
        case4tree = createTreeFromList(["a", "b", "c", "d", "e", "f", "g"])
        logger.debug("deleteDebug - case 4:")
        logger.debug("tree before delete:\n" + printTreeString(case4tree))
        logger.debug("maximum before delete:\n" + case4tree.get_Last().getValue())  # should be g
        case4BalanceOps = case4tree.delete(6)
        logger.debug("tree after delete:\n" + printTreeString(case4tree))
        logger.debug(f"case4 balanceOps: {case4BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case4tree.get_Last().getValue())  # should be c
        self.assertEqual(0, case4BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case4tree, createTreeFromList(["a", "b", "c", "d", "e", "f", None])))

        # Case 5: deleting a one childed node (leftSon)
        case5tree = createTreeFromList(["a", "b", "c", "d", "e", "f", None])
        logger.debug("deleteDebug - case 5:")
        logger.debug("tree before delete:\n" + printTreeString(case5tree))
        logger.debug("maximum before delete:\n" + case5tree.get_Last().getValue())  # should be c
        case5BalanceOps = case5tree.delete(5)
        logger.debug("tree after delete:\n" + printTreeString(case5tree))
        logger.debug(f"case5 balanceOps: {case5BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case5tree.get_Last().getValue())  # should be f
        self.assertEqual(0, case5BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case5tree, createTreeFromList(["a", "b", "f", "d", "e", None, None])))

        # Case 6: deleting a one childed node that is the root (leftSon)
        case6tree = createTreeFromList(["a", "b", None])
        logger.debug("deleteDebug - case 6:")
        logger.debug("tree before delete:\n" + printTreeString(case6tree))
        logger.debug("maximum before delete:\n" + case6tree.get_Last().getValue())  # should be a
        case6BalanceOps = case6tree.delete(1)
        logger.debug("tree after delete:\n" + printTreeString(case6tree))
        logger.debug(f"case6 balanceOps: {case6BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case6tree.get_Last().getValue())  # should be b
        self.assertEqual(0, case6BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case6tree, createTreeFromList(["b"])))

        # Case 7: deleting a one childed node (rightSon)
        case7tree = createTreeFromList(["a", "b", "c", "d", "e", None, "f"])
        logger.debug("deleteDebug - case 7:")
        logger.debug("tree before delete:\n" + printTreeString(case7tree))
        logger.debug("maximum before delete:\n" + case7tree.get_Last().getValue())  # should be f
        case7BalanceOps = case7tree.delete(4)
        logger.debug("tree after delete:\n" + printTreeString(case7tree))
        logger.debug(f"case7 balanceOps: {case7BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case7tree.get_Last().getValue())  # should be f
        self.assertEqual(0, case7BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case7tree, createTreeFromList(["a", "b", "f", "d", "e", None, None])))

        # Case 8: deleting a one childed node that is the root (rightSon)
        case8tree = createTreeFromList(["a", None, "b"])
        logger.debug("deleteDebug - case 8:")
        logger.debug("tree before delete:\n" + printTreeString(case8tree))
        logger.debug("maximum before delete:\n" + case8tree.get_Last().getValue())  # should be b
        logger.debug("minimum before delete:\n" + case8tree.get_First().getValue())  # should be a
        case8BalanceOps = case8tree.delete(0)
        logger.debug("tree after delete:\n" + printTreeString(case8tree))
        logger.debug(f"case8 balanceOps: {case8BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case8tree.get_Last().getValue())  # should be b
        logger.debug("minimum after delete:\n" + case8tree.get_First().getValue())  # should be b
        self.assertEqual(0, case8BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case8tree, createTreeFromList(["b"])))

        # Case 9: deleting a one childed node that was the minimum (rightSon)
        case9tree = createTreeFromList(["a", "b", "c", None, "e", "f", "g"])
        logger.debug("deleteDebug - case 9:")
        logger.debug("tree before delete:\n" + printTreeString(case9tree))
        logger.debug("maximum before delete:\n" + case9tree.get_Last().getValue())  # should be g
        logger.debug("minimum before delete:\n" + case9tree.get_First().getValue())  # should be b
        case9BalanceOps = case9tree.delete(0)
        logger.debug("tree after delete:\n" + printTreeString(case9tree))
        logger.debug(f"case9 balanceOps: {case9BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case9tree.get_Last().getValue())  # should be g
        logger.debug("minimum after delete:\n" + case9tree.get_First().getValue())  # should be e
        self.assertEqual(0, case9BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case9tree, createTreeFromList(["a", "e", "c", None, None, "f", "g"])))

        # Case 10: deleting a two childed node that his successor is a leaf
        case10tree = createTreeFromList(["a", "b", "c", "d", "e", "f", "g"])
        logger.debug("deleteDebug - case 10:")
        logger.debug("tree before delete:\n" + printTreeString(case10tree))
        logger.debug("maximum before delete:\n" + case10tree.get_Last().getValue())  # should be g
        logger.debug("minimum before delete:\n" + case10tree.get_First().getValue())  # should be d
        logger.debug(case10tree.listToArray())
        case10BalanceOps = case10tree.delete(1)
        logger.debug(case10tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(case10tree))
        logger.debug(f"case10 balanceOps: {case10BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case10tree.get_Last().getValue())  # should be g
        logger.debug("minimum after delete:\n" + case10tree.get_First().getValue())  # should be d
        self.assertEqual(0, case10BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case10tree, createTreeFromList(["a", "e", "c", "d", None, "f", "g"])))

        # Case 11: deleting a two childed node that his successor is the maximum
        case11tree = createTreeFromList(["a", "b", "c"])
        logger.debug("deleteDebug - case 11:")
        logger.debug("tree before delete:\n" + printTreeString(case11tree))
        logger.debug("maximum before delete:\n" + case11tree.get_Last().getValue())  # should be c
        logger.debug("minimum before delete:\n" + case11tree.get_First().getValue())  # should be b
        logger.debug(case11tree.listToArray())
        case11BalanceOps = case11tree.delete(1)
        logger.debug(case11tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(case11tree))
        logger.debug(f"case11 balanceOps: {case11BalanceOps}")  # should be 0
        logger.debug("maximum after delete:\n" + case11tree.get_Last().getValue())  # should be c
        logger.debug("minimum after delete:\n" + case11tree.get_First().getValue())  # should be b
        self.assertEqual(0, case11BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case11tree, createTreeFromList(["c", "b", None])))

        # Case 12: deleting a two childed node that his successor has a right child
        case12tree = createTreeFromList(["a", "b", "c", None, None, None, "d"])
        logger.debug("deleteDebug - case 12:")
        logger.debug("tree before delete:\n" + printTreeString(case12tree))
        logger.debug("maximum before delete:\n" + case12tree.get_Last().getValue())  # should be d
        logger.debug("minimum before delete:\n" + case12tree.get_First().getValue())  # should be b
        logger.debug(case12tree.listToArray())
        case12BalanceOps = case12tree.delete(1)
        logger.debug(case12tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(case12tree))
        logger.debug(f"case12 balanceOps: {case12BalanceOps}")  # should be 1
        logger.debug("maximum after delete:\n" + case12tree.get_Last().getValue())  # should be d
        logger.debug("minimum after delete:\n" + case12tree.get_First().getValue())  # should be b
        self.assertEqual(1, case12BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(case12tree, createTreeFromList(["c", "b", "d"])))

        # Case 13: deleting a two childed node that is the root - checked in case 11
        # Cases 14-19 https://visualgo.net/en/bst?mode=AVL&create=16,8,22,4,11,20,24,2,5,9,14,18,21,25,3,10,12,15,17,13
        # Case 14: delete 11 - 2 childed that successor has right child (14 height, 12 height, 8 height, 16 height - total 4)
        cases14to19tree = createTreeFromList([
            "16",
            "8", "22",
            "4", "11", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "12", "15", "17", None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, "13", None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("deleteDebug - case 14:")
        logger.debug("tree before delete:\n" + printTreeString(cases14to19tree))
        logger.debug("maximum before delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum before delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        logger.debug(cases14to19tree.listToArray())
        case14BalanceOps = cases14to19tree.delete(7)
        logger.debug(cases14to19tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(cases14to19tree))
        logger.debug(f"case14 balanceOps: {case14BalanceOps}")  # should be 4
        logger.debug("maximum after delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum after delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        self.assertEqual(4, case14BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(cases14to19tree, createTreeFromList([
            "16",
            "8", "22",
            "4", "12", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "13", "15", "17", None, None, None, None, None, None, None
        ])))

        # Case 15: delete 25 - leaf + maximum (includes right rotation & left then right rotation, 3 ops + 24 changes height - total 4) # TODO: check after evia's rotations
        cases14to19tree = createTreeFromList([
            "16",
            "8", "22",
            "4", "11", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "12", "15", "17", None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, "13", None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("deleteDebug - case 15:")
        logger.debug("tree before delete:\n" + printTreeString(cases14to19tree))
        logger.debug("maximum before delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum before delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        logger.debug(cases14to19tree.listToArray())
        case15BalanceOps = cases14to19tree.delete(19)
        logger.debug(cases14to19tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(cases14to19tree))
        logger.debug(f"case15 balanceOps: {case15BalanceOps}")  # should be 4
        logger.debug("maximum after delete:\n" + cases14to19tree.get_Last().getValue())  # should be 24
        logger.debug("minimum after delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        self.assertEqual(4, case15BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(cases14to19tree, createTreeFromList([
            "11",
            "8", "16",
            "4", "9", "14", "20",
            "2", "5", None, "10", "12", "15", "18", "22",
            None, "3", None, None, None, None, None, None, None, "13", None, None, "17", None, "21", "24"
        ])))

        # Case 16: delete 16 - 2 childed that successor is a leaf + root (18 height, 20 height, 22 height, + leftThenRight - total 5) #TODO: check after evia's rotations
        cases14to19tree = createTreeFromList([
            "16",
            "8", "22",
            "4", "11", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "12", "15", "17", None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, "13", None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("deleteDebug - case 16:")
        logger.debug("tree before delete:\n" + printTreeString(cases14to19tree))
        logger.debug("maximum before delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum before delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        logger.debug(cases14to19tree.listToArray())
        case16BalanceOps = cases14to19tree.delete(12)
        logger.debug(cases14to19tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(cases14to19tree))
        logger.debug(f"case16 balanceOps: {case16BalanceOps}")  # should be 5
        logger.debug("maximum after delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum after delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        self.assertEqual(5, case16BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(cases14to19tree, createTreeFromList([
            "11",
            "8", "17",
            "4", "9", "14", "22",
            "2", "5", None, "10", "12", "15", "20", "24",
            None, "3", None, None, None, None, None, None, None, "13", None, None, "18", "21", None, "25"
        ])))

        # Case 17: delete 24 - one childed node rightSon (rightRotation, leftThenRight - total 3) # TODO: check after evia's rotations
        cases14to19tree = createTreeFromList([
            "16",
            "8", "22",
            "4", "11", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "12", "15", "17", None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, "13", None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("deleteDebug - case 17:")
        logger.debug("tree before delete:\n" + printTreeString(cases14to19tree))
        logger.debug("maximum before delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum before delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        logger.debug(cases14to19tree.listToArray())
        case17BalanceOps = cases14to19tree.delete(18)
        logger.debug(cases14to19tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(cases14to19tree))
        logger.debug(f"case17 balanceOps: {case17BalanceOps}")  # should be 3
        logger.debug("maximum after delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum after delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        self.assertEqual(3, case17BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(cases14to19tree, createTreeFromList([
            "11",
            "8", "16",
            "4", "9", "14", "20",
            "2", "5", None, "10", "12", "15", "18", "22",
            None, "3", None, None, None, None, None, None, None, "13", None, None, "17", None, "21", "25"
        ])))

        # Case 18: delete 18 - one childed node leftSon (20 height, 22 height, leftThenRight - total 4) #TODO: check after evia's rotations
        cases14to19tree = createTreeFromList([
            "16",
            "8", "22",
            "4", "11", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "12", "15", "17", None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, "13", None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("deleteDebug - case 18:")
        logger.debug("tree before delete:\n" + printTreeString(cases14to19tree))
        logger.debug("maximum before delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum before delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        logger.debug(cases14to19tree.listToArray())
        case18BalanceOps = cases14to19tree.delete(14)
        logger.debug(cases14to19tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(cases14to19tree))
        logger.debug(f"case18 balanceOps: {case18BalanceOps}")  # should be 4
        logger.debug("maximum after delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum after delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        self.assertEqual(4, case18BalanceOps)
        # Undependent check
        self.assertTrue(treesEqual(cases14to19tree, createTreeFromList([
            "11",
            "8", "16",
            "4", "9", "14", "22",
            "2", "5", None, "10", "12", "15", "20", "24",
            None, "3", None, None, None, None, None, None, None, "13", None, None, "17", "21", None, "25"
        ])))

        # Case 19: delete 2 - minimum (new minimum should be 3) (4 height, leftRotation, 16 height - total 3) #TODO: check after evia's rotations
        cases14to19tree = createTreeFromList([
            "16",
            "8", "22",
            "4", "11", "20", "24",
            "2", "5", "9", "14", "18", "21", None, "25",
            None, "3", None, None, None, "10", "12", "15", "17", None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, "13", None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None, None, None, None
        ])
        logger.debug("deleteDebug - case 19:")
        logger.debug("tree before delete:\n" + printTreeString(cases14to19tree))
        logger.debug("maximum before delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum before delete:\n" + cases14to19tree.get_First().getValue())  # should be 2
        logger.debug(cases14to19tree.listToArray())
        case19BalanceOps = cases14to19tree.delete(0)
        logger.debug(cases14to19tree.listToArray())
        logger.debug("tree after delete:\n" + printTreeString(cases14to19tree))
        logger.debug(f"case19 balanceOps: {case19BalanceOps}")  # should be 3
        logger.debug("maximum after delete:\n" + cases14to19tree.get_Last().getValue())  # should be 25
        logger.debug("minimum after delete:\n" + cases14to19tree.get_First().getValue())  # should be 3
        self.assertEqual(3, case19BalanceOps)
        self.assertTrue(treesEqual(cases14to19tree, createTreeFromList([
            "16",
            "11", "22",
            "8", "14", "20", "24",
            "4", "9", "12", "15", "18", "21", None, "25",
            "3", "5", None, "10", None, "13", None, None, "17", None, None, None, None, None, None, None
        ])))

    def test_swapNodes(self):
        # Case 1: swapping a root "a" with its successor "b"
        case1tree = createTreeFromList(["a", None, "b"])
        logger.debug(f"Case 1 - tree before swap:\n{printTreeString(case1tree)}")
        node1beforeSwap = case1tree.getRoot()
        node2beforeSwap = case1tree.getRoot().getRight()
        case1tree.swapNodes(node1beforeSwap, node2beforeSwap)
        logger.debug(f"Case 1 - tree after swap:\n{printTreeString(case1tree)}")
        self.assertEqual(case1tree.getRoot(), node2beforeSwap)

        # Case 2: swapping a node "a" with its rightSon "b" (which is the maximum)
        case2tree = createTreeFromList(["a", None, "b"])
        logger.debug(f"Case 2 - tree before swap:\n{printTreeString(case2tree)}")
        node1beforeSwap = case2tree.getRoot()
        node2beforeSwap = case2tree.getRoot().getRight()
        case2tree.swapNodes(node1beforeSwap, node2beforeSwap)
        logger.debug(f"Case 2 - tree after swap:\n{printTreeString(case2tree)}")
        self.assertEqual(case2tree.getRoot(), node2beforeSwap)
        self.assertEqual(case2tree.get_Last(), node1beforeSwap)

        self.assertEqual(case2tree.get_First(), node2beforeSwap)

        # Case 3: swapping a node "a" with its leftSon "b" (which is the minimum)
        case3tree = createTreeFromList(["a", "b", None])
        logger.debug(f"Case 3 - tree before swap:\n{printTreeString(case3tree)}")
        node1beforeSwap = case3tree.getRoot()
        node2beforeSwap = case3tree.getRoot().getLeft()
        case3tree.swapNodes(node1beforeSwap, node2beforeSwap)
        logger.debug(f"Case 3 - tree after swap:\n{printTreeString(case3tree)}")
        self.assertEqual(case3tree.getRoot(), node2beforeSwap)
        self.assertEqual(case3tree.get_First(), node1beforeSwap)

        # Case 4: swapping random 2 nodes "b" and "c"
        case4tree = createTreeFromList(["a", "b", "c", "d", "e", "f", "g"])
        logger.debug(f"Case 4 - tree before swap:\n{printTreeString(case4tree)}")
        node1beforeSwap = case4tree.getRoot().getLeft()
        node2beforeSwap = case4tree.getRoot().getRight()
        case4tree.swapNodes(node1beforeSwap, node2beforeSwap)
        logger.debug(f"Case 4 - tree after swap:\n{printTreeString(case4tree)}")

    if __name__ == "__main__":
        unittest.main()
