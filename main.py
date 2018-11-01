#!/usr/bin/python2.7
import heap

def main():
	h = heap.Heap(10)
	h.backing[0] = heap.HeapObject(4)
	h.backing[1] = heap.HeapObject(1)
	h.backing[2] = heap.HeapObject(3)
	h.backing[3] = heap.HeapObject(2)
	h.backing[4] = heap.HeapObject(16)
	h.backing[5] = heap.HeapObject(9)
	h.backing[6] = heap.HeapObject(10)
	h.backing[7] = heap.HeapObject(14)
	h.backing[8] = heap.HeapObject(8)
	h.backing[9] = heap.HeapObject(7)

	h.heapify()
	print h

	while len(h.backing) != 0:
		print h.extract()

main()
