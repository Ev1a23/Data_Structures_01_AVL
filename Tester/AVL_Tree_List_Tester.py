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

        # Test Case 4: tree has a root and a right node which is a leaf.
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

        # Test Case 6: tree has a root and a left son that has a left son.
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

        # Test Case 7: tree has a root and a right son that has a right son.
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

        # Test Case 8:
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

        # Test Case 9:
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



    if __name__ == "__main__":
        unittest.main()