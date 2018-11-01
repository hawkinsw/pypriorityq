#!/usr/bin/python2.7

class HeapObject(object):
	def __init__(self, priority = 1, value = None):
		self.priority = priority
		self.value = value
	def __repr__(self):
		return str(self.priority) + ": " + repr(self.value)

class Heap(object):
	def __init__(self, size, debug = False):
		self.backing = [HeapObject() for x in range(0, size)]
		self.size = size
		self.debug = debug

	@staticmethod
	def parent(index):
		return int((index-1)/2)

	@staticmethod
	def left(index):
		return 2*index + 1
	
	@staticmethod
	def right(index):
		return 2*index + 2

	def _swap(self, i, j):
		if self.debug:
			print "Swapping " + str(i) + "," + str(j)
		j_value = self.backing[j].value
		j_priority = self.backing[j].priority

		# Put i into j
		self.backing[j].value = self.backing[i].value
		self.backing[j].priority = self.backing[i].priority

		# Put j into i
		self.backing[i].value = j_value
		self.backing[i].priority = j_priority

	def peek(self):
		return (self.backing[0].priority, self.backing[0].value)

	def extract(self):
		result = (self.backing[0].priority, self.backing[0].value)
	
		self.size -= 1
		self.backing = self.backing[1:]

		if self.size != 0:
			self._heapify(0)

		return result

	def heapify(self):
		for index in range(int(self.size/2), -1, -1):
			if self.debug:
				print "Calling _heapify(self, " + str(index) + ")\n"
			self._heapify(index)

	def __repr__(self):
		repr = ""
		for index in range(0,self.size):
			repr += str(index) + ":" + str(self.backing[index]) + "\n"
		return repr

	def _heapify(self, index):
		if self.debug:
			print "index: " + str(index)
		l = Heap.left(index)
		r = Heap.right(index)
		if l<self.size:
			if self.debug:
				print "l: " + str(l) + " (" + str(self.backing[l].priority) + ")"
		if r<self.size:
			if self.debug:
				print "r: " + str(r) + " (" + str(self.backing[r].priority) + ")"
		largest = index
		if l < self.size and self.backing[l].priority > self.backing[index].priority:
			# Our left child is larger than we are!
			largest = l
		if r < self.size and self.backing[r].priority > self.backing[largest].priority:
			# Our right child is the largest!
			largest = r
	
		if self.debug:
			print "largest: " + str(largest) + " (" + str(self.backing[largest].priority) + ")"
		if largest != index:
			self._swap(largest, index)
			self._heapify(largest)

def test():
	h = Heap(10)
	h.backing[0] = HeapObject(4)
	h.backing[1] = HeapObject(1)
	h.backing[2] = HeapObject(3)
	h.backing[3] = HeapObject(2)
	h.backing[4] = HeapObject(16)
	h.backing[5] = HeapObject(9)
	h.backing[6] = HeapObject(10)
	h.backing[7] = HeapObject(14)
	h.backing[8] = HeapObject(8)
	h.backing[9] = HeapObject(7)

	h.heapify()
	print h

	while len(h.backing) != 0:
		print h.extract()

if __name__=="__main__":
	test()
