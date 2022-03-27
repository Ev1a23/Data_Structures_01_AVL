#username - eviatars
#id1      - 322623182
#name1    - Eviatar Shemesh
#id2      - 208392290
#name2    - Yoav Malichi



"""A class represnting a node in an AVL tree"""

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
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		if self.isRealNode():
			return self.value
		return None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
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
	"""
	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
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
	"""
	def isRealNode(self):
		return self.height != -1



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return None


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
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

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
	As we saw in the lecture the time complexity analysis is in the worst case O(h) = O(logn).
	"""
	def successor(self, node):
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
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root


