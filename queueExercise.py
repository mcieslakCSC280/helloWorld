from notelec14 import Node, linkedList

class Queue(linkedList):
	def __init__(self, head = None, tail = None):
		super().__init__(head)
		self.tail = tail

	def enq(self, inpd):
		if(self.head == None and self.tail == None):
			newNode = Node(data = inpd, nextNode = None)
			self.size +=1
			self.tail = newNode
			self.head = newNode
		else:
			newNode = Node(data = inpd, nextNode = self.tail)
			self.tail = newNode
			self.size +=1


	def deq(self):
		currentNode = self.head
		nextNode = currentNode.getNext()

		self.head = nextNode
		currentNode.setNext(d = None)
		self.size -= 1
		return(currentNode.getData())

def main():
	myQueue = Queue()
	myQueue.enq(inpd = 100)
	myQueue.enq(inpd = 1000)
	myQueue.enq(inpd = "AU")
	myQueue.enq(inpd = "GW")

	print(myQueue.getSize())

	myQueue.deq()
	print(myQueue.getSize())

	



if __name__ == '__main__':
	main()