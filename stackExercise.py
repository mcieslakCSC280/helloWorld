from notelec14 import Node, linkedList

class Stack(linkedList):
	def __init__(self, head = None):
		super().__init__(head)

	def push(self, inpd):
		newNode = Node(data = inpd, nextNode = self.head)
		self.head = newNode
		self.size +=1

	def pop(self):
		currentNode = self.head
		nextNode = currentNode.getNext()

		self.head = nextNode
		currentNode.setNext(d = None)
		self.size -= 1
		return(currentNode.getData())

def main():
	myStack = Stack()
	myStack.push(inpd = 100)
	myStack.push(inpd = 1000)
	myStack.push(inpd = "AU")
	myStack.push(inpd = "GW")

	print(myStack.pop())
	print(myStack.getSize())

	print(myStack.pop())
	print(myStack.getSize())



if __name__ == '__main__':
	main()