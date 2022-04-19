from avl_skeleton import AVLTreeList as Balanced
import unbalancedTree as Unbalanced
import random

random.seed(10)


def balanced_generator():
    limiter = 1
    while True:
        for i in range(0, 2 ** limiter, 2):
            yield i
        limiter += 1


print("Results:\n")

for i in range(1, 11):
    print("i=", i)
    balanced1 = Balanced.AVLTreeList()  # insert at start
    balanced2 = Balanced.AVLTreeList()  # insert balanced
    balanced3 = Balanced.AVLTreeList()  # insert random
    unbalanced1 = Unbalanced.AVLTreeList()  # insert at start
    unbalanced2 = Unbalanced.AVLTreeList()  # insert balanced
    unbalanced3 = Unbalanced.AVLTreeList()  # insert random
    #######################################
    ############## AT START ###############
    #######################################
    cntbalanced1 = 0
    cntunbalanced1 = 0
    cntdepth1 = 0
    cntdepth2 = 0
    for j in range(1000 * i, 0, -1):
        res1 = balanced1.insert2(0, j)
        res2 = unbalanced1.insert2(0, j)
        cntbalanced1 += res1[0]
        cntunbalanced1 += res2[0]
        cntdepth1 += res1[1]
        cntdepth2 += res2[1]
    print("Average balance ops for AVL tree insert at start= ", cntbalanced1 / (1000 * i))
    print("Average balance ops for Unbalanced tree insert at start= ", cntunbalanced1 / (1000 * i))
    print("")
    print("Average depth for AVL tree insert at start= ", cntdepth1 / (1000 * i))
    print("Average depth for Unbalanced tree insert at start= ", cntdepth2 / (1000 * i))
    print("")
    print("")

    #######################################
    ############## Balanced ###############
    #######################################
    ### we insert at 0 -> 0,2 -> 0,2,4,6 -> ......
    cntbalanced2 = 0
    cntunbalanced2 = 0
    cntdepth3 = 0
    cntdepth4 = 0
    k = 0
    gen = balanced_generator()
    while k < 1000 * i:
        j = next(gen)
        res3 = balanced2.insert2(j, j)
        res4 = unbalanced2.insert2(j, j)
        cntbalanced2 += res3[0]
        cntunbalanced2 += res4[0]
        cntdepth3 += res3[1]
        cntdepth4 += res4[1]
        k += 1
    print("Average balance ops for AVL tree balanced inserts= ", cntbalanced2 / (1000 * i))
    print("Average balance ops for Unbalanced tree balanced inserts= ", cntunbalanced2 / (1000 * i))
    print("")
    print("Average depth for AVL tree balanced inserts= ", cntdepth3 / (1000 * i))
    print("Average depth for Unbalanced tree  balanced inserts= ", cntdepth4 / (1000 * i))
    print("")
    print("")

    #######################################
    ############### Random ################
    #######################################
    cntbalanced3 = 0
    cntunbalanced3 = 0
    cntdepth5 = 0
    cntdepth6 = 0
    for j in range(1000 * i):
        r = random.randrange(0, 1 + j)
        res5 = balanced3.insert2(r, r)
        res6 = unbalanced3.insert2(r, r)
        cntbalanced3 += res5[0]
        cntunbalanced3 += res6[0]
        cntdepth5 += res5[1]
        cntdepth6 += res6[1]
    print("Average balance ops for AVL tree random inserts= ", cntbalanced3 / (1000 * i))
    print("Average balance ops for Unbalanced tree random inserts= ", cntunbalanced3 / (1000 * i))
    print("")
    print("Average depth for AVL tree random inserts= ", cntdepth5 / (1000 * i))
    print("Average depth for Unbalanced tree random inserts= ", cntdepth6 / (1000 * i))
    print("")
    print("")
    del balanced1, balanced2, balanced3, unbalanced1, unbalanced2, unbalanced3
