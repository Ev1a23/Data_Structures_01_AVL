#username - eviatars
#id1      - 322623182
#name1    - Eviatar Shemesh
#id2      - 208392290
#name2    - Yoav Malichi


"""A class representing a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.size = 0
		self.height = -1


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	@Time complexity: O(1)
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	@Time complexity: O(1)
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	@Time complexity: O(1)
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	@Time complexity: O(1)
	"""
	def getValue(self):
		if self.isRealNode():
			return self.value
		return None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	@Time complexity: O(1)
	"""
	def getHeight(self):
		if self.isRealNode():
			return self.height
		return -1

	"""returns the size

	@rtype: int
	@returns: the size of self, virtual node size is 0
	"""

	def getSize(self):
		return self.size

	"""returns the balance factor of a given node 

	@rtype: int
	@returns: height of left child of self - height of right child of self, 0 if virtual node
	"""

	def getBalanceFactor(self):
		if self.isRealNode():
			return self.getLeft().height - self.getRight().height
		return 0

	"""recomputes the size of a Node inplace
	
	@returns: None
	"""
	def recomputeSize(self):
		if self.isRealNode():
			self.size = self.left.size + 1 + self.right.size

	"""recomputes the height of a Node inplace

	@returns: None
	"""

	def recomputeHeight(self):
		if self.isRealNode():
			self.height = max(self.left.height, self.right.height) + 1

	"""sets left child

	@type node: AVLNode
	@param node: a node
	@Time complexity: O(1)
	"""
	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	@Time complexity: O(1)
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	@Time complexity: O(1)
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	@Time complexity: O(1)
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	@Time complexity: O(1)
	"""
	def setHeight(self, h):
		self.height = h

	"""sets the size of the node

	@type s: int
	@param s: the size 
	"""

	def setSize(self, s):
		self.size = s
	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	@Time complexity: O(1)
	"""
	def isRealNode(self):
		return self.height != -1

	""" returns true whether self is a leaf
	
		@rtype: bool
		@returns: False if self is not a leaf (has a right/left son such that they are not virtual nodes), True otherwise
		@Time complexity: O(1)
		"""

	def isLeaf(self):
		return self.getHeight() == 0

	# Used for testing only
	def __eq__(self, other):
		if other is None:
			return False
		return self.getHeight() == other.getHeight() and self.getSize() == other.getSize() and self.getValue() == other.getValue()



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.first_node = None
		self.last_node = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	@Time complexity: O(1)
	"""
	def empty(self):
		return self.root is None

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	
	Time Complexity:
	Recursion that in worst case goes every call goes one son left / one son right until the deepest leaf
	Meaning that the maximum calls is the height of tree
	In every recursion call there is O(1) work, and the height of the tree is O(logn)
	That is why, in total, as we saw in the lecture, the time complexity is O(logn) in the worst case
	"""
	def retrieve(self, i):

		root = self.getRoot()

		def retrieveRec(node, j):
			loc = node.left.size + 1

			if loc == j:
				return node.getValue()
			elif j < loc:
				return retrieveRec(node.left, j)
			else:
				return retrieveRec(node.right, j - loc)

		return retrieveRec(root, i + 1)

	"""retrieves the AVLNode that is the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: AVLNode
	@returns: the AVLNode that is the i'th item in the list

	Time Complexity:
	Recursion that in worst case goes every call goes one son left / one son right until the deepest leaf
	Meaning that the maximum calls is the height of tree
	In every recursion call there is O(1) work, and the height of the tree is O(logn)
	That is why, in total, as we saw in the lecture, the time complexity is O(logn) in the worst case
	"""

	def retrieveNode(self, i):

		root = self.getRoot()

		def retrieveRec(node, j):
			loc = node.left.size + 1

			if loc == j:
				return node
			elif j < loc:
				return retrieveRec(node.left, j)
			else:
				return retrieveRec(node.right, j - loc)

		return retrieveRec(root, i + 1)

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		return -1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	
	@Time Complexity:
	successor - called once - O(logn) [see successor]
	swapNodes - O(1)
	reBalance - called once - O(logn) [see reBalance]
	Others - O(1)
	Total: O(logn)
	"""
	def delete(self, i):
		nodeToDelete = self.retrieveNode(i)
		if nodeToDelete.isLeaf(): # case 1 - lecture 2 slide 51
			nodeToDeleteParent = nodeToDelete.getParent()
			if nodeToDelete is self.getRoot():
				self.root = None
				self.set_Last(None)
				self.set_First(None)
				return 0
			if nodeToDelete is self.get_First():
				self.set_First(nodeToDeleteParent)
			if nodeToDelete is self.get_Last():
				self.set_Last(nodeToDeleteParent)
			nodeToDelete.setParent(None)
			if nodeToDeleteParent.getLeft() is nodeToDelete:
				nodeToDeleteParent.setLeft(AVLNode(None))
			elif nodeToDeleteParent.getRight() is nodeToDelete:
				nodeToDeleteParent.setRight(AVLNode(None))
			balanceOps = self.reBalance(nodeToDeleteParent, 'delete')
		elif nodeToDelete.getLeft().isRealNode() and not nodeToDelete.getRight().isRealNode(): # case 2.1 - lecture 2 slide 51
			nodeToDeleteParent = nodeToDelete.getParent()
			nodeToDeleteLeftSon = nodeToDelete.getLeft()
			nodeToDeleteLeftSon.setParent(nodeToDeleteParent)
			if nodeToDelete is self.get_Last():
				self.set_Last(nodeToDeleteLeftSon.maximum())
			nodeToDelete.setLeft(AVLNode(None))
			nodeToDelete.setParent(None)
			if self.getRoot() is nodeToDelete: # i.e. nodeToDeleteParent is None
				self.root = nodeToDeleteLeftSon
			else:
				nodeToDeleteParent.setLeft(nodeToDeleteLeftSon)
			balanceOps = self.reBalance(nodeToDeleteParent, 'delete')
		elif nodeToDelete.getRight().isRealNode() and not nodeToDelete.getLeft().isRealNode(): # case 2.2 - lecture 2 slide 51
			nodeToDeleteParent = nodeToDelete.getParent()
			nodeToDeleteRightSon = nodeToDelete.getRight()
			nodeToDeleteRightSon.setParent(nodeToDeleteParent)
			if nodeToDelete is self.get_First():
				self.set_First(nodeToDeleteRightSon.minimum())
			nodeToDelete.setRight(AVLNode(None))
			nodeToDelete.setParent(None)
			if self.getRoot() is nodeToDelete: # i.e. nodeToDeleteParent is None
				self.root = nodeToDeleteRightSon
			else:
				nodeToDeleteParent.setRight(nodeToDeleteRightSon)
			balanceOps = self.reBalance(nodeToDeleteParent, 'delete')
		else: # case 3 - lecture 2 slide 51
			nodeToDeleteSuccessor = self.successor(nodeToDelete)
			if not nodeToDeleteSuccessor.isLeaf(): # i.e. it has 1 right child only (if 2 then it wasn't the successor)
				self.swapNodes(nodeToDelete, nodeToDeleteSuccessor)
				nodeToDeleteParent = nodeToDelete.getParent()
				nodeToDeleteRightSon = nodeToDelete.getRight()
				nodeToDeleteRightSon.setParent(nodeToDeleteParent)
				if nodeToDelete is self.get_First():
					self.set_First(nodeToDeleteSuccessor)
				nodeToDelete.setRight(AVLNode(None))
				nodeToDelete.setParent(None)
				if self.getRoot() is nodeToDelete:  # i.e. nodeToDeleteParent is None
					self.root = nodeToDeleteRightSon
				else:
					nodeToDeleteParent.setRight(nodeToDeleteRightSon)
				balanceOps = self.reBalance(nodeToDeleteParent, 'delete')
			else:
				self.swapNodes(nodeToDelete, nodeToDeleteSuccessor)
				nodeToDeleteParent = nodeToDelete.getParent()
				nodeToDelete.setParent(None)
				if nodeToDeleteParent.getLeft() is nodeToDelete:
					nodeToDeleteParent.setLeft(AVLNode(None))
				elif nodeToDeleteParent.getRight() is nodeToDelete:
					nodeToDeleteParent.setRight(AVLNode(None))
				balanceOps = self.reBalance(nodeToDeleteParent, 'delete')

		return balanceOps

	""" Swapping 2 nodes (changing pointers)
	
	@type node1: AVLNode
	@param node1: an AVLNode
	@post node1: node1.getParent() == @prevnode2.getParent(),
	node1.getLeft() == @prevnode2.getLeft(),
	node1.getRight() == @prevnode2.getRight()
	node1.getSize() == @prevnode2.getSize()
	node1.getHeight() == @prevnode2.getHeight()
	
	@type node2: AVLNode
	@param node2: an AVLNode
	@post node2: node2.getParent() == @prevnode1.getParent(),
	node2.getLeft() == @prevnode1.getLeft(),
	node2.getRight() == @prevnode1.getRight()
	node2.getSize() == @prevnode1.getSize()
	node2.getHeight() == @prevnode1.getHeight() 
	
	@rtype: None
	"""
	def swapNodes(self, node1, node2):
		node1Parent = node1.getParent()
		node1Left = node1.getLeft()
		node1Right = node1.getRight()
		if node1Parent:
			if node1Parent.getLeft() is node1:
				node1Parent.setLeft(node2)
			elif node1Parent.getRight() is node1:
				node1Parent.setRight(node2)

		node2Parent = node2.getParent()
		node2Left = node2.getLeft()
		node2Right = node2.getRight()
		if node2Parent:
			if node2Parent.getLeft() is node2:
				node2Parent.setLeft(node1)
			elif node2Parent.getRight() is node2:
				node2Parent.setRight(node1)

		node2.setLeft(node1Left)
		node1Left.setParent(node2)
		node2.setRight(node1Right)
		node1Right.setParent(node2)
		node2.setParent(node1Parent)

		node1.setLeft(node2Left)
		node2Left.setParent(node1)
		node1.setRight(node2Right)
		node2Right.setParent(node1)
		node1.setParent(node2Parent)

		node1.recomputeSize()
		node1.recomputeHeight()
		node2.recomputeSize()
		node2.recomputeSize()

	"""Re balancing the Tree inplace
	
	@type treeOp: str
	@pre: treeOp in ['insert', 'delete']
	@param treeOp: The tree operation that called reBalance ('insert'/'delete')
	
	@type nodeToCheckBF: AVLNode
	@param nodeToCheckBF: The start node in which we'll start to rebalance the tree up to the root (if needed)
	
	@rtype: int
	@return: number of balancing operations that have been made in order to reBalance the tree
	
	@Time complexity:
	Worst case - maximum route from a node to root is O(h) = O(logn)
	In every node in that route, O(1) work is executed in the worst case (rotation + arithmetic operation)
	Total: O(logn) * O(1) = O(logn) work
	"""
	def reBalance(self, nodeToCheckBF, treeOp):
		balanceOps = 0
		if treeOp == 'insert':
			# TODO: eviatar decide if after insert we go all the way to the top in order to update sizes, as for now it goes all the way up, we can delete treeOp if so.
			while nodeToCheckBF is not None:
				balanceFactor = nodeToCheckBF.getBalanceFactor()
				height = nodeToCheckBF.getHeight()
				if abs(balanceFactor) == 2:
					balanceOps += self.rotate(nodeToCheckBF, balanceFactor)
					# break
				elif abs(balanceFactor) < 2:
					nodeToCheckBF.recomputeHeight()
					nodeToCheckBF.recomputeSize()
					if nodeToCheckBF.getHeight() != height:
						balanceOps += 1
				nodeToCheckBF = nodeToCheckBF.getParent()

		elif treeOp == 'delete':
			while nodeToCheckBF is not None:
				balanceFactor = nodeToCheckBF.getBalanceFactor()
				height = nodeToCheckBF.getHeight()
				if abs(balanceFactor) == 2:
					balanceOps += self.rotate(nodeToCheckBF, balanceFactor)
				elif abs(balanceFactor) < 2:
					nodeToCheckBF.recomputeHeight()
					nodeToCheckBF.recomputeSize()
					if nodeToCheckBF.getHeight() != height:
						balanceOps += 1
				nodeToCheckBF = nodeToCheckBF.getParent()

		return balanceOps

	""" Applies the correct rotation to the tree, during rebalance process
	  
	@type BFcriminal: AVLNode
	@pre: BFcriminal is not None
	@param BFcriminal: a node that its BalanceFactor violating the AVLTreeList balance rules (+2/-2)
	
	@type balanceFactor: int
	@param balanceFactor: the balance factor of BFcriminal
	
	@rtype: int
	@return: number of balancing operations that took place
	"""

	def rotate(self, BFcriminal, balanceFactor):
		balanceOps = 0
		if balanceFactor == 2:
			if BFcriminal.getLeft().getBalanceFactor in [0, 1]:
				self.rightRotation(BFcriminal)
				balanceOps += 1
			elif BFcriminal.getLeft().getBalanceFactor == -1:
				self.leftThenRightRotation(BFcriminal)
				balanceOps += 2

		elif balanceFactor == -2:
			if BFcriminal.getLeft().getBalanceFactor in [-1, 0]:
				self.leftRotation(BFcriminal)
				balanceOps += 1
			elif BFcriminal.getLeft().getBalanceFactor == 1:
				self.rightThenLeftRotation(BFcriminal)
				balanceOps += 2
		return balanceOps


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	@Time complexity: O(1)
	"""
	def first(self):
		if self.first_node is not None:
			return self.first_node.getValue()
		return None

	"""returns a pointer to the first node
	@rtype: AVLNode
	@Time complexity: O(1)
	"""
	def get_First(self):
		return self.first_node

	"""sets the first item of the list to a given node
	
	@param node: a pointer to a AVLNode
	@Time complexity: O(1)
	"""
	def set_First(self, node):
		self.first_node = node

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	@Time complexity: O(1)
	"""
	def last(self):
		if self.last_node is not None:
			return self.last_node.getValue()
		return None

	"""return a pointer to the last item in the list
	@param node: a pointer to AVLNode
	@Time complexity: O(1)
	"""
	def get_Last(self):
		return self.last_node

	"""sets the last item of the list to a given node
	
	@param node: a pointer to a node
	@Time complexity: O(1)
	"""
	def set_Last(self, node):
		self.last_node = node


	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	
	Time Complexity:
	Initiliazing an empty list - O(1)
	get_First() - returns an attribute of self, without any calculations - O(1)
	
	Conclusion from recitation 3 ex 3 - starting at the minimal element of a tree and calling n-1 times to successor
	is O(n) work since we go through every edge (there are n-1 edges) at most 2 times.
	Plus,
		node is not None - O(1), n times -> O(n)
		lst.append(node.getValue()) - O(1), n times -> O(n)
		
	Therefore, the entire while loop takes O(n) time in the worst case.
	"""
	def listToArray(self):
		lst = []
		node = self.get_First()
		while node is not None:
			lst.append(node.getValue())
			node = self.successor(node)
		return lst

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		if not self.empty():
			return self.root.getSize()
		# returns 0 if list is empty
		return 0

	"""returns the successor of a given node
	
	@pre: node.isRealNode() == True
	@type node: AVLNode
	@param node: the node of which we will return its successor
	@rtype: AVLNode
	@returns: The successor of node, None if node is the last element in the list
	
	Time complexity:
	As we saw in the lecture the time complexity analysis is in the worst case O(h) = O(logn)
	In case that node == self.get_Last() then O(1)
	"""
	def successor(self, node):
		if node == self.get_Last():
			return None

		x = node
		if x.getRight().isRealNode():
			return self.minimum(x.getRight())
		y = x.getParent()
		while y is not None and x == y.right:
			x = y
			y = x.parent
		return y

	"""returns the minimum of a given sub tree that node is its root
	i.e. the deepest node that is on the `/` branch that starts from node
	
	@pre: node.isRealNode() == True
	@type node: AVLNode
	@param node: the node of which we will return the minimum of his subtree
	@rtype: AVLNode
	@returns: The minimum of node's subtree, if it is a leaf, returns itself
	
	Time complexity:
	minimum = node - O(1)
	(*) minimum.getLeft() is not None && minimum = minimum.getLeft() are O(1) each
	(*) is executed at most as many times as the height of the tree.
	Therefore, the total time complexity is O(h) = O(logn).
	"""
	def minimum(self, node):
		minNode = node
		while minNode.getLeft().isRealNode():
			minNode = minNode.getLeft()
		return minNode

	"""returns the maximum of a given sub tree that node is its root
		i.e. the deepest node that is on the `\` branch that starts from node

		@pre: node.isRealNode() == True
		@type node: AVLNode
		@param node: the node of which we will return the maximum of his subtree
		@rtype: AVLNode
		@returns: The maximum of node's subtree, if it is a leaf, returns itself

		Time complexity:
		maximum = node - O(1)
		(*) maxNode.getRight() is not None && maxNode = maxNode.getRight() are O(1) each
		(*) is executed at most as many times as the height of the tree.
		Therefore, the total time complexity is O(h) = O(logn).
		"""

	def maximum(self, node):
		maxNode = node
		while maxNode.getRight().isRealNode():
			maxNode = maxNode.getRight()
		return maxNode


	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	
	@Time complexity:
	Worst case:
	delete - called once - O(logn)
	insert - called once - O(logn)
	join - called once - O(logn)
	"""
	def concat(self, lst):
		selfHeight = -1 if self.getRoot() is None else self.getRoot().getHeight()
		lstHeight = -1 if lst.getRoot() is None else lst.getRoot().getHeight()
		absHeightDiff = abs(lstHeight - selfHeight)

		if self.empty():
			self.root = lst.getRoot()
			return absHeightDiff

		if lst.empty():
			return absHeightDiff

		x = self.get_Last()

		if self.getRoot() is x and self.length() == 1:
			self.delete(self.getRoot().getSize() - 1)
			lst.insert(0, x.getValue())
			self.root = lst.getRoot()
			return absHeightDiff

		self.delete(self.getRoot().getSize() - 1)
		self.join(self, x, lst)

		return absHeightDiff

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	@Time complexity: O(n) worst case (list to array(O(n), iterate through the array: O(n)) 
	"""
	def search(self, val):
		if self.empty():
			return -1
		if self.first() == val:
			return 0
		lst = self.listToArray() #O(n), see listToArray time complexity
		i = 0
		for x in lst:
			if x == val:
				return i
			i += 1
		return -1

	"""performs a right rotation inplace
	
	@pre: called from reBalance function (due to a tree operation)
	
	@type BFcriminal: AVLNode
	@pre: BFcriminal has a left son (performed on nodes that their BF is at least 1)
	@param BFcriminal: node that violates the balance rules of an AVL tree
	@post BFcriminal: node won't violate the balance rules of an AVL tree anymore
	
	@rtype: None
	"""
	def rightRotation(self, BFcriminal):
		BFcriminalLeftSon = BFcriminal.getLeft()

		# B.left <- A.right
		BFcriminal.setLeft(BFcriminalLeftSon.getRight())

		# B.left.parent <- B
		BFcriminal.getLeft().setParent(BFcriminal)

		# A.right <- B
		BFcriminalLeftSon.setRight(BFcriminal)

		# A.parent <- B.parent
		BFcriminalLeftSon.setParent(BFcriminal.getParent())

		# A.parent.left/right <- A
		if BFcriminal.getParent() is None:
			self.root = BFcriminalLeftSon

		elif BFcriminal.getParent().getLeft() == BFcriminal:
			BFcriminal.getParent().setLeft(BFcriminalLeftSon)

		elif BFcriminal.getParent().getRight() == BFcriminal:
			BFcriminal.getParent().setRight(BFcriminalLeftSon)

		# B.parent <- A
		BFcriminal.setParent(BFcriminalLeftSon)

		# Recomputes size & height
		BFcriminal.recomputeSize()
		BFcriminal.recomputeHeight()
		BFcriminalLeftSon.recomputeSize() # A.size <- B.size
		BFcriminalLeftSon.recomputeHeight()

	"""performs a left then right rotation inplace
	
	@pre: called from reBalance function (due to a tree operation)
	
	@type BFcriminal: AVLNode
	@pre: BFcriminal's BF is +2 (i.e. it has a real left son) and left son BF is -1 (i.e. it has a real right son)
	@param BFcriminal: node that violates the balance rules of an AVL tree
	@post BFcriminal: node won't violate the balance rules of an AVL tree anymore
	
	@rtype: None
	"""

	def leftThenRightRotation(self, BFcriminal):
		self.leftRotation(BFcriminal.getLeft())
		self.rightRotation(BFcriminal)

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	@Time complexity: O(1)
	"""
	def getRoot(self):
		if self.root is not None:
			return self.root
		return None

	""" find the predecessor of a given node
	@param - AVLNode
	@return - AVLNode, the predecessor of the node. if it's the first node, return null
	@Time complexity: O(logn) worst case, go through the height of the tree(logn), each move O(1) work(pointers switch)
	if our node is the first node of the tree, O(1) time complexity 
	"""
	def predecessor(self, node):
		if not node.isRealNode():
			return None
		if self.get_First() == node:
			return None
		if node.getLeft() is not None and node.getLeft().isRealNode():
			help = node.getLeft()
			while help.getRight() is not None and help.getRight().isRealNode():
				help = help.getRight()
			return help

		help = node.getParent()
		while help is not None and help.isRealNode():
			if help.getRight() == node:
				return help
			node = help
			help = help.getParent()
		return None

	# Used for testing only
	"""Checks if current AVLTreeList is equals to another AVLTreeList
	Definition: AVLTreeList are considered equal if trees size are equal 
	and recursively checking that currentTreeRoot == otherTreeRoot (by checking their values, size, and height) 
	& currentTreeRoot.left equals otherTreeRoot.left
	& currentTreeRoot.right equals otherTreeRoot.right
	
	@type other: AVLTreeList
	@param other: an AVLTreeList to compare self to
	@returns: True if trees are equal, False otherwise
	@rtype: boolean
	"""

	def __eq__(self, other):
		if (not isinstance(other, AVLTreeList)) or other.length() != self.length():
			return False

		currentRoot = self.getRoot()
		otherRoot = other.getRoot()

		if currentRoot is None and otherRoot is None:
			return True

		def equalsRec(currentRoot, otherRoot):
			if currentRoot != otherRoot:
				return False

			if not currentRoot.isRealNode() and not otherRoot.isRealNode():
				return True

			return equalsRec(currentRoot.getLeft(), otherRoot.getLeft()) and equalsRec(currentRoot.getRight(), otherRoot.getRight())

		return equalsRec(currentRoot, otherRoot)

