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
		self.height = -1


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	@time complexity: O(1)
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	@time complexity: O(1)
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	@time complexity: O(1)
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	@time complexity: O(1)
	"""
	def getValue(self):
		if self.isRealNode():
			return self.value
		return None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	@time complexity: O(1)
	"""
	def getHeight(self):
		if self.isRealNode():
			return self.height
		return -1

	"""sets left child

	@type node: AVLNode
	@param node: a node
	@time complexity: O(1)
	"""
	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	@time complexity: O(1)
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	@time complexity: O(1)
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	@time complexity: O(1)
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	@time complexity: O(1)
	"""
	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	@time complexity: O(1)
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
		self.first_node = None
		self.last_node = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	@time complexity: O(1)
	"""
	def empty(self):
		return self.root is None

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return None

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
	@time complexity: O(1)
	"""
	def first(self):
		if self.first_node is not None:
			return self.first_node.getValue()
		return None

	"""returns a pointer to the first node
	@rtype: AVLNode
	@time complexity: O(1)
	"""
	def get_First(self):
		return self.first_node

	"""sets the first item of the list to a given node
	
	@param node: a pointer to a AVLNode
	@time complexity: O(1)
	"""
	def set_First(self, node):
		self.first_node = node

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	@time complexity: O(1)
	"""
	def last(self):
		if self.last_node is not None:
			return self.last_node.getValue()
		return None

	"""return a pointer to the last item in the list
	@param node: a pointer to AVLNode
	@time complexity: O(1)
	"""
	def get_Last(self):
		return self.last_node

	"""sets the last item of the list to a given node
	
	@param node: a pointer to a node
	@time complexity: O(1)
	"""
	def set_Last(self, node):
		self.last_node = node


	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return None

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
	@time complexity: O(n) worst case (list to array(O(n), iterate through the array: O(n)) 
	"""
	def search(self, val):
		if(self.empty()):
			return -1
		if(self.getRoot().getValue() == val):
			return self.getRoot().getLeft().getSize() #need to implement size property and get size in AVLNode
		if(self.first() == val):
			return 0
		if(self.last() == val):
			return self.root.getSize()-1
		lst = self.listToArray() #O(n), recitaion 04, waiting for implementaion by yoav
		i =0
		for x in lst:
			if(x.getValue() == val):
				return i
			i+=1
		return -1





	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	@time complexity: O(1)
	"""
	def getRoot(self):
		if self.root is not None:
			return self.root
		return None

	""" find the predecessor of a given node
	@param - AVLNode
	@return - AVLNode, the predecessor of the node. if it's the first node, return null
	@time complexity: O(logn) worst case, go through the height of the tree(logn), each move O(1) work(pointers switch) 
	"""
	def predecessor(self, node):
		if node.isRealNode()== False:
			return None
		if(self.get_First() == node):
			return None
		if(node.getLeft()!= None and node.getLeft().isRealNode()):
			help = node.getLeft()
			while(help.getRight()!= None and help.getRight().isRealNode()):
				help = help.getRight()
			return help

		if(node.getParent().getRight() !=None and node.getParent().getRight() == node):
			return node.getParent()
		help = node.getParent()
		while(help!=None and help.isRealNode()):
			if(help.getRight() == node):
				return help
			node = help
			help = help.getParent()
		return None








