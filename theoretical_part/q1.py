from avl_skeleton import AVLTreeList as AVLTreeList
import random
import sys


def exp1():
    results = []
    ###### First Exp - Insertions ########
    print("---------------First Exp--------------")
    for i in range (1, 11):
        experimental = AVLTreeList()
        cnt = experimental.insert(0, "0")
    # Insert 1000*2^i nodes randomly
        for j in range (1000*(2**i)-1):
            r = random.randint(0,experimental.length()-1)
            cnt += experimental.insert(r, str(r))
        print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)
        results.append(cnt)
    print("--------------------------------------")
    return results

def exp2():
    results = []
    print("---------------Second Exp--------------")
    ####### Second Exp - Deletions ########
    for i in range (1, 11):
        experimental = AVLTreeList()
        experimental.insert(0, "0")
    # Insert 1000*2^i nodes randomly
        for j in range (1000*(2**i)-1):
            r = random.randint(0,experimental.length()-1)
            experimental.insert(r, str(r))
        cnt=0
    # Delete all nodes in a random order:
        for k in range (1000*(2**i)):
            r = random.randint(0,experimental.length()-1)
            cnt += experimental.delete(r)
        print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)
        results.append(cnt)
    print("--------------------------------------")
    return results

def exp3():
    ###### Third Exp - Insertions/Deletions ########
    results= []
    print("------------Third Exp-------------")
    for i in range (1, 11):
        experimental = AVLTreeList()
        experimental.insert(0, "0")
    # Insert 1000*2^i nodes randomly
        for j in range (1000*(2**(i-1))-1):
            r = random.randint(0,experimental.length()-1)
            experimental.insert(r, str(r))
        cnt=0
        for k in range (int(1000*(2**(i-2)))):
            if experimental.length()!=(1000*(2**(i-1))):
                print(r)
                return [experimental, r]
            try:
                r = random.randint(0,experimental.length()-1)
                cnt += experimental.insert(r, str(r))
                r = random.randint(0,experimental.length()-1)
                cnt += experimental.delete(r)
            except Exception:
                o = sys.exc_info()
        print ("For tree with 1000*2^",i,"nodes, number of 'Balance Ops' is:", cnt)
        results.append(cnt)
    return results

# f = open("/Users/orshemesh/DS_projects/resultsQ1.txt", 'w')
#
#res1 = exp1()
#res2 = exp2()
res3 = exp3()
# for i in range(10):
#     f.write(str(res1[i])+","+str(res2[i])+","+str(res3[i])+"\n")
#
# f.close()

