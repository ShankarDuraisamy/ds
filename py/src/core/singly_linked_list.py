class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def __str__(self):
		temp = self.head
		expr = "[ "
		while temp:
			expr += f"{temp.data} "
			temp = temp.next
		expr += ']'
		return expr

	def append(self, node: Node):
		if self.head is None:
			self.head = node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = node

	def prepend(self, node: Node):
		if self.head is None:
			self.head = node
		else:
			temp = self.head
			self.head = node
			self.head.next = temp

	def insert_at_position(self, position, node):
		temp = self.head
		count = 0
		while temp and count < position:
			count += 1
			temp = temp.next
		if not count == position:
			raise Exception("Linked List Error :: Invalid Position")
		else:
			node.next = temp.next
			temp.next = node

	def pop(self):
		result = None
		if self.head is None:
			raise Exception("No Element in the list.")
		else:
			temp = self.head
			previous_node = None
			while temp.next and temp.next.next:
				temp = temp.next
			temp.next = Node
			if not temp.next.next:
				result = temp.next.value
				temp.next = None
			else:
				result = temp.next.next.value
				temp.next.next = None
		return result

	def length(self, recursive: bool = True):
		return self.length_recursive(self.head) if recursive else self.length_iterative()

	def length_recursive(self, node, count=0):
		if not node:
			return count
		else:
			return self.length_recursive(node.next, count + 1)

	def length_iterative(self):
		node = self.head
		count = 0
		while node:
			count = 1
			node = node.next
		return count


def main():
	node_1 = Node(1)
	node_2 = Node(2)
	node_3 = Node(3)
	node_4 = Node(4)
	list = LinkedList(node_1)
	print(f"value = {list}, length={list.length()}")
	list.append(node_2)
	print(f"value = {list}, length={list.length()}")
	list.prepend(node_3)
	print(f"value = {list}, length={list.length()}")
	list.insert_at_position(2, node_4)
	print(f"value = {list}, length={list.length()}")


if __name__ == "__main__":
	main()
