import unittest
import avl_skeleton as file
from avl_skeleton import AVLNode
from avl_skeleton import AVLTreeList

class Test_AVL_Tree_list(unittest.TestCase):
    # def test_Empty(self):
    #     tree = AVLTreeList()
    #     self.assertEqual(True, tree.empty())
    #     root = AVLNode("3")
    #     tree.root = root
    #     self.assertEqual(False, tree.empty())
    #     root.height = 3
    #     self.assertEqual(False, tree.empty())
    #     root.setValue(5)
    #     self.assertEqual(False, tree.empty())
    #     tree.root = None
    #     self.assertEqual(True, tree.empty())
    #
    # def test_length(self):
    #     tree = AVLTreeList()
    #
    #     # Test Case 1: root is None. expected length: 0.
    #     self.assertEqual(0, tree.length())
    #
    #     # Test Case 2: root is not None, size of root is 10. expected length: 10.
    #     root = AVLNode("3")
    #     tree.root = root
    #     self.assertEqual(10, tree.length())

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
        self.assertEqual(root, tree.retrieve(0))

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
        self.assertEqual(lSon, tree.retrieve(0))
        self.assertEqual(root, tree.retrieve(1))

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
        self.assertEqual(root, tree.retrieve(0))
        rlSon = AVLNode("4")
        rSon.setLeft(rlSon)
        self.assertEqual(rSon, tree.retrieve(1))

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
        self.assertEqual(llSon, tree.retrieve(0))
        self.assertEqual(lSon, tree.retrieve(1))
        self.assertEqual(root, tree.retrieve(2))

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
        self.assertEqual(root, tree.retrieve(0))
        self.assertEqual(rSon, tree.retrieve(1))
        self.assertEqual(rrSon, tree.retrieve(2))

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
        self.assertEqual(lSon, tree.retrieve(0))
        self.assertEqual(lrSon, tree.retrieve(1))
        self.assertEqual(root, tree.retrieve(2))
        self.assertEqual(rSon, tree.retrieve(3))

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
        self.assertEqual(lSon, tree.retrieve(0))
        self.assertEqual(root, tree.retrieve(1))
        self.assertEqual(rlSon, tree.retrieve(2))
        self.assertEqual(rSon, tree.retrieve(3))

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

    # def test_listToArray(self):
    #     tree = AVLTreeList()
    #     root = AVLNode("3")
    #     root.setSize(1)
    #     root.setHeight(0)
    #     lSon = AVLNode("2")
    #     rSon = AVLNode("4")
    #     virtualNode = AVLNode(None)
    #     root.setLeft(lSon)
    #     root.setRight(rSon)
    #     tree.root = root
    #
    #     # Test Case 1: tree has only 1 node - root. i = 0. expected: ["3"].
    #     #         root
    #     #        /    \
    #     #       ---   ---
    #     self.assertEqual(["3"], tree.listToArray())
    #     root.setValue("kk")
    #     self.assertEqual(["kk"], tree.listToArray())
    #     root.setValue("3")
    #
    #     # Test Case 2: tree has a root and a left node which is a leaf.
    #     #              root
    #     #           /        \
    #     #          l         ---
    #     #        /    \
    #     #       ---  ---
    #     # expected: ["2","3"].
    #     lSon.setHeight(0)
    #     lSon.setSize(1)
    #     llSon = AVLNode("3")
    #     lSon.setLeft(llSon)
    #     lSon.setRight(virtualNode)
    #     root.setSize(2)
    #     self.assertEqual(["2","3"], tree.listToArray())
    #
    #     # Test Case 3: tree has a root and a right node which is a leaf.
    #     #             root
    #     #           /      \
    #     #         ---        r
    #     #                  /    \
    #     #                 ---  ---
    #     # expected: ["3", "4"]
    #     lSon.setHeight(-1)
    #     lSon.setSize(0)
    #     rSon.setHeight(0)
    #     rSon.setSize(1)
    #     rSon.setLeft(virtualNode)
    #     rSon.setRight(virtualNode)
    #     self.assertEqual(["3", "4"], tree.listToArray())
    #     rlSon = AVLNode("4")
    #     rSon.setLeft(rlSon)
    #
    #     # Test Case 4: tree has a root and a left son that has a left son.
    #     #                        root
    #     #                     /       \
    #     #                   l         ---
    #     #                 /   \
    #     #               ll     ---
    #     #             /   \
    #     #           ---   ---
    #     # expected: ["3", "2", "3"]
    #     lllSon = AVLNode("3")
    #     llSon.setLeft(lllSon)
    #     llSon.setRight(virtualNode)
    #     llSon.setHeight(0)
    #     llSon.setSize(1)
    #     lSon.setSize(2)
    #     root.setSize(3)
    #     rSon.setHeight(-1)
    #     self.assertEqual(["3", "2", "3"], tree.listToArray())
    #
    #     # Test Case 5: tree has a root and a right son that has a right son.
    #     #                        root
    #     #                     /       \
    #     #                   ---         r
    #     #                             /   \
    #     #                            ---   rr
    #     #                                /    \
    #     #                              ---    ---
    #     # expected: ["3", "4", "3"]
    #     rrSon = AVLNode("3")
    #     rSon.setRight(rrSon)
    #     rrlSon = AVLNode("3")
    #     rrSon.setLeft(rrlSon)
    #     rrSon.setHeight(0)
    #     rrSon.setSize(1)
    #     rSon.setSize(2)
    #     root.setSize(3)
    #     lSon.setHeight(-1)
    #     lSon.setSize(0)
    #     self.assertEqual(["3", "4", "3"], tree.listToArray())
    #
    #     # Test Case 6:
    #     #                        root
    #     #                     /       \
    #     #                   l           r
    #     #                 /   \       /   \
    #     #               ----   lr    -------
    #     #                    /   \
    #     #                   -------
    #     # expected: ["2", "3", "3", "4"]
    #     virtualNode = AVLNode("1")
    #     rSon.setHeight(0)
    #     rSon.setSize(1)
    #     rSon.setLeft(virtualNode)
    #     rSon.setRight(virtualNode)
    #
    #     lSon.setHeight(1)
    #     lSon.setSize(2)
    #     lSon.setLeft(virtualNode)
    #
    #     lrSon = AVLNode("3")
    #     lrSon.setHeight(0)
    #     lrSon.setSize(1)
    #     lrSon.setLeft(virtualNode)
    #     lrSon.setRight(virtualNode)
    #     lSon.setRight(lrSon)
    #
    #     root.setHeight(2)
    #     root.setSize(4)
    #     self.assertEqual(["2","3","3","4"], tree.listToArray())
    #
    #     # Test Case 7:
    #     #                        root
    #     #                     /       \
    #     #                   l           r
    #     #                 /   \       /   \
    #     #                -------    rl   ----
    #     #                          /   \
    #     #                         -------
    #     # expected: ["2", "3", "4", "5"], changing r's value to "5"
    #     lSon.setHeight(0)
    #     lSon.setSize(1)
    #     lSon.setLeft(virtualNode)
    #     lSon.setRight(virtualNode)
    #
    #     rSon.setHeight(1)
    #     rSon.setSize(2)
    #     rSon.setRight(virtualNode)
    #     rSon.setValue("5")
    #
    #     rlSon = AVLNode("4")
    #     rlSon.setHeight(0)
    #     rlSon.setSize(1)
    #     rlSon.setLeft(virtualNode)
    #     rlSon.setRight(virtualNode)
    #     rSon.setLeft(rlSon)
    #
    #     root.setHeight(2)
    #     root.setSize(4)
    #     self.assertEqual(["2", "3", "4", "5"], tree.listToArray())


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


    if __name__ == "__main__":
        unittest.main()