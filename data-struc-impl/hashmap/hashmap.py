class HashMap:
	# create empty bucket list of given size
	def __init__(self, size):
		self.size = size
		self.hashmap = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range(self.size)]

	def hash_key(self, key):
		return hash(key) % self.size

	# insert values into hashmap using seperate chaining
	def insert(self, key, value):
		# get the index from the key using pythons built in hash function
		hashed_key = self.hash_key(self, key)
		self.hashmap[hashed_key].append(value)

	def search(self, key):
		hashed_key = self.hash_key(self, key)
		return self.hashmap[hashed_key].search(key)

	def delete(self, key):
		hashed_key = self.hash_key(self, key)
		return self.hashmap[hashed_key].remove(key)

	# def resize():