########################################
## Question 2 in the theoretical part ##
########################################
from avl_skeleton import AVLTreeList as AVLTreeList
import math
import random
print("Results of the analysis:")
for i in range(1,11):
    ### each iteration represents a different size of the tree ####
    tree1=AVLTreeList.AVLTreeList()
    tree2=AVLTreeList.AVLTreeList()
    for j in range(1000*(2**i)):
        r=random.randrange(0, 1+j)
        tree1.insert(r,r)
        tree2.insert(r,r)
    ##### Random split ####
    r=random.randrange(0,tree1.length())
    res1=tree1.splitExp(r)
    avg1=res1[3]
    max1=res1[4]
    ##### Splitting the maximum node of the left son of the tree #####
    res2=tree2.splitExp(tree2.getRoot().getLeft().getSize()-1)
    avg2=res2[3]
    max2=res2[4]
    print("i = "+ str(i))
    print("Maximum join cost of random splitted tree is: ",max1 )
    print("Average join cost of random splitted tree is: ",avg1 )
    print("Maximum join cost of split maximum of left sub-tree of the root: ",max2 )
    print("Average join cost of split maximum of left sub-tree of the root: ",avg2 )
    del tree1, tree2
