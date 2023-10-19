class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def inorder(self):
		if self.left:
			self.left.postorder()
		print(self.value)
		if self.right:
			self.right.postorder()

	def postorder(self):
		if self.left:
			self.left.postorder()

		if self.right:
			self.right.postorder()
		
		print(self.value)

	def preorder(self):
		print(self.value)
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()

	def insert(self, value):
		if self.value:
			if value < self.value:
				if self.left is None:
					self.left = BinarySearchTree(value)
				else:
					self.left.insert(value)
			elif value > self.value:
				if self.right is None:
					self.right = BinarySearchTree(value)
				else:
					self.right.insert(value)
		else:
			self.value = value

	def search(self, value):
		if value < self.value:
			if self.left is None:
				# print("Not Found") 
				return False
			return self.left.search(value)
		elif value > self.value:
			if self.right is None:
				# print("Not Found") 
				return False
			return self.right.search(value)
		else:
			return True

	def delete(self, value):
		if not self:
			return self
		if self.value > value:
			self.left = self.left.delete(value)
		elif self.value < value:
			self.right = self.right.delete(value)
		else:
			if not self.right:
				return self.left
			if not self.left:
				return self.right
			temp = self.right
			min = temp.value
			while temp.left:
				temp = temp.left
				min = temp.value
			self.right = self.right.delete(self.value)
		return self

if __name__ == "__main__":
	bst = BinarySearchTree(5)
	bst.insert(6)
	bst.insert(3)
	bst.insert(57)
	bst.insert(1)
	bst.insert(29)
	bst.inorder()
	print(bst.search(1))
	bst.delete(1)
	print(bst.search(1))
