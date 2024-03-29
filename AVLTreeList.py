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

	"""sets the height of the node

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
		@returns: False if self is not a leaf (has a right/left son such that they are not virtual nodes), 
		True otherwise
		@Time complexity: O(1)
		"""

	def isLeaf(self):
		return self.getHeight() == 0



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor

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
	@param val: the value we insert
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	def insert(self, i, val):
		inserted = AVLNode(val)
		inserted.setHeight(0)
		inserted.setSize(1)
		virtualL = AVLNode("")
		virtualR = AVLNode("")
		inserted.setLeft(virtualL)
		inserted.setRight(virtualR)
		virtualL.setParent(inserted)
		virtualR.setParent(inserted)

		#insterted node will be root
		if(self.empty()):
			self.root = inserted
			self.set_First(inserted)
			self.set_Last(inserted)
			inserted.recomputeHeight()
			inserted.recomputeSize()
			return 0

		#insert at the begin of list
		if i == 0:
			node = self.get_First()
			node.setLeft(inserted)
			inserted.setParent(node)
			self.set_First(inserted)
			return self.reBalance(node)


		#insert at end of list
		elif i == self.length():
			node = self.get_Last()
			node.setRight(inserted)
			inserted.setParent(node)
			self.set_Last(inserted)
			return self.reBalance(node)

		#get current i'th node
		node = self.retrieveNode(i)

		#has left son, need to insert right of the predecessor, has no right son
		if node.getLeft().isRealNode():
			node = self.predecessor(node)
			node.setRight(inserted)
			inserted.setParent(node)
			return self.reBalance(node)

		#insert as left son of i'th node
		else:
			node.setLeft(inserted)
			inserted.setParent(node)
			return self.reBalance(node)

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	
	@Time Complexity worst case:
	successor - called once - O(logn) [see successor]
	swapNodes - O(1)
	deleteLeaf - called once - O(logn) [see deleteLeaf]
	deleteOneChildedNode - called once - O(logn [see deleteOneChildedNode]
	Others - O(1)
	Total: O(logn)
	"""
	def delete(self, i):
		nodeToDelete = self.retrieveNode(i)
		if nodeToDelete.isLeaf(): # case 1 - lecture 2 slide 51
			return self.deleteLeaf(nodeToDelete, '1')
		elif nodeToDelete.getLeft().isRealNode() and not nodeToDelete.getRight().isRealNode(): # case 2.1 - lecture 2 slide 51
			return self.deleteOneChildedNode(nodeToDelete, 'left')
		elif nodeToDelete.getRight().isRealNode() and not nodeToDelete.getLeft().isRealNode(): # case 2.2 - lecture 2 slide 51
			return self.deleteOneChildedNode(nodeToDelete, 'right')
		else: # case 3 - lecture 2 slide 51
			nodeToDeleteSuccessor = self.successor(nodeToDelete)
			if not nodeToDeleteSuccessor.isLeaf(): # i.e. it has 1 right child only (if 2 then it wasn't the successor)
				self.swapNodes(nodeToDelete, nodeToDeleteSuccessor)
				return self.deleteOneChildedNode(nodeToDelete, 'right')
			else:
				self.swapNodes(nodeToDelete, nodeToDeleteSuccessor)
				return self.deleteLeaf(nodeToDelete, '3')

	""" deletes a node that has one child (bypass)
	
	@type nodeToDelete: AVLNode
	@pre: nodeToDelete is not None and has only one real child
	@param nodeToDelete: node to delete
	
	@type childSide: str
	@param childSide: nodeToDelete's child side is real node, and the other child is virtual
	
	@rtype: int
	@return: total balance operations that were required during the delete operation
	@Time complexity worst case:
	O(1) - getters & setters
	reBalance - O(logn) [see reBalance]
	successor / predecessor - O(logn)
	total: O(logn)
	"""
	def deleteOneChildedNode(self, nodeToDelete, childSide):
		if childSide == 'left':
			nodeToDeleteParent = nodeToDelete.getParent()
			nodeToDeleteLeftSon = nodeToDelete.getLeft()
			if nodeToDelete is self.get_Last():
				self.set_Last(self.predecessor(nodeToDelete))
			nodeToDeleteLeftSon.setParent(nodeToDeleteParent)
			nodeToDelete.setLeft(AVLNode(None))
			nodeToDelete.getLeft().setParent(nodeToDeleteLeftSon)
			nodeToDelete.setParent(None)
			if self.getRoot() is nodeToDelete:  # i.e. nodeToDeleteParent is None
				self.root = nodeToDeleteLeftSon
			else:
				if nodeToDeleteParent.getLeft() is nodeToDelete:
					nodeToDeleteParent.setLeft(nodeToDeleteLeftSon)
				elif nodeToDeleteParent.getRight() is nodeToDelete:
					nodeToDeleteParent.setRight(nodeToDeleteLeftSon)
			balanceOps = self.reBalance(nodeToDeleteParent)

		elif childSide == 'right':
			nodeToDeleteParent = nodeToDelete.getParent()
			nodeToDeleteRightSon = nodeToDelete.getRight()
			if nodeToDelete is self.get_First(): # irrelevant in case 3
				self.set_First(self.successor(nodeToDelete))
			nodeToDeleteRightSon.setParent(nodeToDeleteParent)
			nodeToDelete.setRight(AVLNode(None))
			nodeToDelete.getRight().setParent(nodeToDeleteRightSon)
			nodeToDelete.setParent(None)
			if self.getRoot() is nodeToDelete:  # i.e. nodeToDeleteParent is None
				self.root = nodeToDeleteRightSon
			else:
				if nodeToDeleteParent.getLeft() is nodeToDelete:
					nodeToDeleteParent.setLeft(nodeToDeleteRightSon)
				elif nodeToDeleteParent.getRight() is nodeToDelete:
					nodeToDeleteParent.setRight(nodeToDeleteRightSon)
			balanceOps = self.reBalance(nodeToDeleteParent)

		return balanceOps

	""" deletes a node that is a leaf

		@type nodeToDelete: AVLNode
		@pre: nodeToDelete is not None and has 2 virtual sons
		@param nodeToDelete: node to delete

		@type case: str
		@param case: case 1 / 3 (original node is a leaf / successor is a leaf respectively)

		@rtype: int
		@return: total balance operations that were required during the delete operation
		
		@Time complexity:
		O(1) - getters & setters
		reBalance - O(logn) [see reBalance]
		predecessor - O(logn)
		successor - O(logn)
		total: O(logn)
		"""
	def deleteLeaf(self, nodeToDelete, case):
		nodeToDeleteParent = nodeToDelete.getParent()
		if case == '1':
			if nodeToDelete is self.getRoot():
				self.root = None
				self.set_Last(None)
				self.set_First(None)
				return 0

		if nodeToDelete is self.get_First():
			self.set_First(self.successor(nodeToDelete))
		if nodeToDelete is self.get_Last():
			self.set_Last(self.predecessor(nodeToDelete))

		nodeToDelete.setParent(None)
		if nodeToDeleteParent.getLeft() is nodeToDelete:
			nodeToDeleteParent.setLeft(AVLNode(None))
			nodeToDeleteParent.getLeft().setParent(nodeToDeleteParent)
		elif nodeToDeleteParent.getRight() is nodeToDelete:
			nodeToDeleteParent.setRight(AVLNode(None))
			nodeToDeleteParent.getRight().setParent(nodeToDeleteParent)
		balanceOps = self.reBalance(nodeToDeleteParent)
		return balanceOps


	""" Swapping 2 nodes (changing pointers)
	
	@pre: boths node1, node2 are AVLNodes
	
	@type node1: AVLNode
	@param node1: an AVLNode
	
	@type node2: AVLNode
	@param node2: an AVLNode
	
	@rtype: None
	"""

	def swapNodes(self, node1, node2):
		node1Parent = node1.getParent()
		node1Left = node1.getLeft()
		node1Right = node1.getRight()

		node2Parent = node2.getParent()
		node2Left = node2.getLeft()
		node2Right = node2.getRight()

		done = False
		# case node1Parent == node2Parent
		# do not switch node1, node2 parents, just switch left and right of parent & sons
		if node1Parent and node2Parent and node1Parent is node2Parent:
			if node1Parent.getLeft() is node1:
				node1Parent.setLeft(node2)
				node1Parent.setRight(node1)
			elif node1Parent.getRight() is node1:
				node1Parent.setRight(node2)
				node1Parent.setLeft(node1)
			node1.setLeft(node2Left)
			node2Left.setParent(node1)
			node1.setRight(node2Right)
			node2Right.setParent(node1)
			node2.setLeft(node1Left)
			node1Left.setParent(node2)
			node2.setRight(node1Right)
			node1Right.setParent(node2)
			done = True

		# if we get here then node1Parent is not node2Parent
		else:
			if node1Parent:
				if node1Parent.getLeft() is node1:
					if node1Parent is not node2:
						node1Parent.setLeft(node2)
					else:
						if node2Parent:
							if node2Parent.getLeft() is node2:
								node2Parent.setLeft(node1)
							elif node2Parent.getRight() is node2:
								node2Parent.setRight(node1)
						node1.setParent(node2Parent)
						node1.setLeft(node2)
						node1.setRight(node2Right)
						node2Right.setParent(node1)

						node2.setLeft(node1Left)
						node1Left.setParent(node2)
						node2.setRight(node1Right)
						node1Right.setParent(node2)
						node2.setParent(node1)

						done = True

				elif node1Parent.getRight() is node1:
					if node1Parent is not node2:
						node1Parent.setRight(node2)
					else:
						if node2Parent:
							if node2Parent.getLeft() is node2:
								node2Parent.setLeft(node1)
							elif node2Parent.getRight() is node2:
								node2Parent.setRight(node1)
						node1.setParent(node2Parent)
						node1.setRight(node2)
						node1.setLeft(node2Left)
						node2Left.setParent(node1)

						node2.setLeft(node1Left)
						node1Left.setParent(node2)
						node2.setRight(node1Right)
						node1Right.setParent(node2)
						node2.setParent(node1)

						done = True

			if node2Parent:
				if node2Parent.getLeft() is node2:
					if node2Parent is not node1:
						node2Parent.setLeft(node1)
					else:
						if node1Parent:
							if node1Parent.getLeft() is node1:
								node1Parent.setLeft(node2)
							elif node1Parent.getRight() is node1:
								node1Parent.setRight(node2)
						node2.setParent(node1Parent)
						node2.setLeft(node1)
						node2.setRight(node1Right)
						node1Right.setParent(node2)

						node1.setLeft(node2Left)
						node2Left.setParent(node1)
						node1.setRight(node2Right)
						node2Right.setParent(node1)
						node1.setParent(node2)

						done = True

				elif node2Parent.getRight() is node2:
					if node2Parent is not node1:
						node2Parent.setRight(node1)
					else:
						if node1Parent:
							if node1Parent.getLeft() is node1:
								node1Parent.setLeft(node2)
							elif node1Parent.getRight() is node1:
								node1Parent.setRight(node2)

						node2.setParent(node1Parent)
						node2.setRight(node1)
						node2.setLeft(node1Left)
						node1Left.setParent(node2)

						node1.setLeft(node2Left)
						node2Left.setParent(node1)
						node1.setRight(node2Right)
						node2Right.setParent(node1)

						node1.setParent(node2)

						done = True

		if not done:
			node1.setParent(node2Parent)
			node1.setLeft(node2Left)
			node1.setRight(node2Right)
			node2Left.setParent(node1)
			node2Right.setParent(node1)

			node2.setParent(node1Parent)
			node2.setLeft(node1Left)
			node2.setRight(node1Right)
			node1Left.setParent(node2)
			node1Right.setParent(node2)

		if self.getRoot() is node1:
			self.root = node2
		elif self.getRoot() is node2:
			self.root = node1

		if self.get_First() is node1:
			self.set_First(node2)
		elif self.get_First() is node2:
			self.set_First(node1)

		if self.get_Last() is node1:
			self.set_Last(node2)
		elif self.get_Last() is node2:
			self.set_Last(node1)

		node1.recomputeSize()
		node1.recomputeHeight()
		node2.recomputeSize()
		node2.recomputeHeight()

	"""Re balancing the Tree inplace
	
	@type nodeToCheckBF: AVLNode
	@param nodeToCheckBF: The start node in which we'll start to rebalance the tree up to the root (if needed)
	
	@rtype: int
	@return: number of balancing operations that have been made in order to reBalance the tree
	
	@Time complexity:
	Worst case - maximum route from a node to root is O(h) = O(logn)
	In every node in that route, O(1) work is executed in the worst case (rotation + arithmetic operation)
	Total: O(logn) * O(1) = O(logn) work
	"""
	def reBalance(self, nodeToCheckBF):
		balanceOps = 0
		while nodeToCheckBF is not None:
			balanceFactor = nodeToCheckBF.getBalanceFactor()
			height = nodeToCheckBF.getHeight()
			if abs(balanceFactor) == 2:
				balanceOps += self.rotate(nodeToCheckBF, balanceFactor)
				nodeToCheckBF = nodeToCheckBF.getParent()
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
			if BFcriminal.getLeft().getBalanceFactor() in [0, 1]:
				self.rightRotation(BFcriminal)
				balanceOps += 1
			elif BFcriminal.getLeft().getBalanceFactor() == -1:
				self.leftThenRightRotation(BFcriminal)
				balanceOps += 2

		elif balanceFactor == -2:
			if BFcriminal.getRight().getBalanceFactor() in [-1, 0]:
				self.leftRotation(BFcriminal)
				balanceOps += 1
			elif BFcriminal.getRight().getBalanceFactor() == 1:
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
	
	Conclusion from recitation 3 ex 3 - starting at the minimal element of a tree and calling 
	n-1 times to successor
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
	(*) maximum.getRight() is not None && maximum = maximum.getRight() are O(1) each
	(*) is executed at most as many times as the height of the tree.
	Therefore, the total time complexity is O(h) = O(logn).
	"""
	def maximum(self, node):
		maxNode = node
		while maxNode.getRight().isRealNode():
			maxNode = maxNode.getRight()
		return maxNode

	"""
	find left subtree with height h
	help function for join
	@pre - h>=0
	@rtype: AVLNode
	Time complexity: O(self.getRoot().getHeight()-h)
	"""
	def find_left_subtree_heightH(self, h):
		if self.getRoot().getHeight() == h:
			return self.getRoot()
		node = self.getRoot()
		help = node
		while h<help.getHeight():
			if help.getLeft().isRealNode():
				help = help.getLeft()
			else:
				return help.getLeft()
		return help

	"""
	find right subtree with height h
	help function for join
	@pre - h>=0
	@rtype: AVLNode
	Time complexity: O(self.getRoot().getHeight()-h)
	"""
	def find_right_subtree_heightH(self, h):
		if self.getRoot().getHeight() == h:
			return self
		node = self.getRoot()
		help = node
		while h<help.getHeight():
			if help.getRight().isRealNode():
				help = help.getRight()
			else:
				return help.getRight()
		return help

	"""
	Join 2 trees T1,T2 with a connector node x
	@pre: T1<x<T2
	@pre: x.isRealNode() == True
	Time complexity: O(abs(height(T2)-Height(T1))+1)
	@returns: tuple, index 0 is the joined tree, index 1 is the number of rebalances
	"""
	@staticmethod
	def join(T1, x, T2):
		new_tree = AVLTreeList()
		x.setParent(None)
		vlNode = AVLNode("")
		vlNode.setParent(x)
		vrNode = AVLNode("")
		vrNode.setParent(x)
		x.setRight(vrNode)
		x.setLeft(vlNode)
		new_tree.root = x
		new_tree.set_First(x)
		new_tree.set_Last(x)
		x.recomputeHeight()
		x.recomputeSize()
		#if one of the trees is an empty tree
		if T1.empty() and T2.empty():
			return new_tree, 0
		elif T1.empty() or T2.empty():
			if T1.empty():
				balances = T2.insert(0, x.getValue())
				return T2, balances
			else:
				balances = T1.insert(T1.length(), x.getValue())
				return T1, balances
		t1h = T1.getRoot().getHeight()
		t2h = T2.getRoot().getHeight()

		#heights are equal
		if t1h == t2h:
			x.setLeft(T1.getRoot())
			x.setRight(T2.getRoot())
			T1.getRoot().setParent(x)
			T2.getRoot().setParent(x)
			x.recomputeHeight()
			x.recomputeSize()
			new_tree.set_First(T1.get_First())
			new_tree.set_Last(T2.get_Last())
			return new_tree, 1

		#t1 height < t2 height
		elif t1h<t2h:
			node = T2.find_left_subtree_heightH(t1h)
			x.setLeft(T1.getRoot())
			x.setRight(node)
			help = node.getParent()
			T1.getRoot().setParent(x)
			node.setParent(x)
			x.setParent(help)
			help.setLeft(x)
			x.recomputeHeight()
			x.recomputeSize()
			new_tree.set_First(T1.get_First())
			new_tree.set_Last(T2.get_Last())
			new_tree.root = T2.getRoot()
			rebalances = new_tree.reBalance(help)
			return new_tree, rebalances

		#t2 height < t1 height
		else:
			node = T1.find_right_subtree_heightH(t2h)
			x.setLeft(node)
			x.setRight(T2.getRoot())
			help = node.getParent()
			T2.getRoot().setParent(x)
			node.setParent(x)
			x.setParent(help)
			help.setRight(x)
			x.recomputeHeight()
			x.recomputeSize()
			new_tree.set_First(T1.get_First())
			new_tree.set_Last(T2.get_Last())
			new_tree.root = T1.getRoot()
			rebalances = new_tree.reBalance(help)
			return new_tree, rebalances

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	Time comlexity: O(logn) with efficient joins as in L03S107
	"""
	def split(self, i):
		balances = 0
		node = self.retrieveNode(i)
		val = node.getValue()
		L = AVLTreeList()
		L.root =node.getLeft()

		R = AVLTreeList()
		R.root = node.getRight()

		help = node.getParent()
		while help is not None:
			if help.getLeft() == node:
				lSon, rSon = True, False
			else:
				lSon, rSon = False, True
			save = help.getParent()
			if rSon:
				L, tmp = AVLTreeList.join(self.create_tree_from_node(help.getLeft()), help, L)
			else:
				R, tmp = AVLTreeList.join(R, help, self.create_tree_from_node(help.getRight()))
			node = help
			help = save
			balances +=tmp

		if L.getRoot() is not None and L.getRoot().isRealNode():
			L.getRoot().setParent(None)
			if L.getRoot().getLeft() is not None and L.getRoot().getLeft().isRealNode():
				L.set_First(L.minimum(L.getRoot()))
			else:
				L.set_First(L.getRoot())
				L.getRoot().setLeft(AVLNode(None))
				L.getRoot().getLeft().setParent(L.getRoot())
			if L.getRoot().getRight() is not None and L.getRoot().getRight().isRealNode():
				L.set_Last(L.maximum(L.getRoot()))
			else:
				L.set_Last(L.getRoot())
				L.getRoot().setRight(AVLNode(None))
				L.getRoot().getRight().setParent(L.getRoot())
		else:
			L = AVLTreeList()
		if R.getRoot() is not None and R.getRoot().isRealNode():
			R.getRoot().setParent(None)
			if R.getRoot().getLeft() is not None and R.getRoot().getLeft().isRealNode():
				R.set_First(R.minimum(R.getRoot()))
			else:
				R.set_First(R.getRoot())
				R.getRoot().setLeft(AVLNode(None))
				R.getRoot().getLeft().setParent(R.getRoot())
			if R.getRoot().getRight() is not None and R.getRoot().getRight().isRealNode():
				R.set_Last(R.maximum(R.getRoot()))
			else:
				R.set_Last(R.getRoot())
				R.getRoot().setRight(AVLNode(None))
				R.getRoot().getRight().setParent(R.getRoot())
		else:
			R = AVLTreeList()
		return [L, val, R]


	"""
	Create a tree that his root is a given node
	@param: AVLnode
	@pre - node.isRealNode() == True
	@returns: a tree t which t.getRoot() == node
	Time complexity: O(1)
	"""


	def create_tree_from_node(self, node):
		node.setParent(None)
		t = AVLTreeList()
		t.root = node
		return t

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
	Total: O(logn)
	"""
	def concat(self, lst):
		selfHeight = -1 if self.getRoot() is None else self.getRoot().getHeight()
		lstHeight = -1 if lst.getRoot() is None else lst.getRoot().getHeight()
		absHeightDiff = abs(lstHeight - selfHeight)

		if self.empty():
			self.root = lst.getRoot()
			self.set_First(lst.get_First())
			self.set_Last(lst.get_Last())
			return absHeightDiff

		if lst.empty():
			return absHeightDiff

		x = self.get_Last()

		self.delete(self.getRoot().getSize() - 1)
		joinedTree = AVLTreeList.join(self, x, lst)[0]

		self.root = joinedTree.getRoot()
		self.set_First(joinedTree.get_First())
		self.set_Last(joinedTree.get_Last())

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

	"""performs a left rotation inplace

	@pre: called from reBalance function (due to a tree operation)

	@type BFcriminal: AVLNode
	@pre: BFcriminal has a right son (performed on nodes that their BF is at least 1)
	@param BFcriminal: node that violates the balance rules of an AVL tree
	@post BFcriminal: node won't violate the balance rules of an AVL tree anymore

	@rtype: None
	"""
	def leftRotation(self, BFcriminal):
		BFcriminalRightSon = BFcriminal.getRight()

		#B.right <- A.left
		BFcriminal.setRight(BFcriminalRightSon.getLeft())

		#B.right.parent <- B
		BFcriminal.getRight().setParent(BFcriminal)

		#A.left <- B
		BFcriminalRightSon.setLeft(BFcriminal)

		#A.parent <- B.parent
		BFcriminalRightSon.setParent(BFcriminal.getParent())

		#A.parent.left/right <- A
		if BFcriminal.getParent() is None:
			self.root = BFcriminalRightSon

		elif BFcriminal.getParent().getRight() == BFcriminal:
			BFcriminal.getParent().setRight(BFcriminalRightSon)

		elif BFcriminal.getParent().getLeft() == BFcriminal:
			BFcriminal.getParent().setLeft(BFcriminalRightSon)

		#B.parent <-A
		BFcriminal.setParent(BFcriminalRightSon)

		#Recomputes size & height
		BFcriminal.recomputeSize()
		BFcriminal.recomputeHeight()
		BFcriminalRightSon.recomputeSize() #A.size <- B.size
		BFcriminalRightSon.recomputeHeight()


	"""performs a left then right rotation inplace
	
	@pre: called from reBalance function (due to a tree operation)
	
	@type BFcriminal: AVLNode
	@pre: BFcriminal's BF is +2 (i.e. it has a real left son) and left son BF is -1 
	(i.e. it has a real right son)
	@param BFcriminal: node that violates the balance rules of an AVL tree
	@post BFcriminal: node won't violate the balance rules of an AVL tree anymore
	
	@rtype: None
	"""

	def leftThenRightRotation(self, BFcriminal):
		self.leftRotation(BFcriminal.getLeft())
		self.rightRotation(BFcriminal)

	"""performs a right then left rotation inplace

	@pre: called from reBalance function (due to a tree operation)

	@type BFcriminal: AVLNode
	@pre: BFcriminal's BF is -2 (i.e. it has a real right son) and right son BF is +1 
	(i.e. it has a real left son)
	@param BFcriminal: node that violates the balance rules of an AVL tree
	@post BFcriminal: node won't violate the balance rules of an AVL tree anymore
	
	@rtype: None
	"""

	def rightThenLeftRotation(self, BFcriminal):
		self.rightRotation(BFcriminal.getRight())
		self.leftRotation(BFcriminal)

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
	@Time complexity: O(logn) worst case, go through the height of the tree(logn), 
	each move O(1) work(pointers switch)
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