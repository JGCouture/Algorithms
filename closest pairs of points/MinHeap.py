class MinHeap:
    def heapify_arr(self, array):
        # Transform an array to a heap with O(len(array)).
        n = len(array)
        for i in reversed(range(n // 2)):
            self.sift_up(array, i)

    def sift_up(self, array, i):
        endpos = len(array)
        startpos = i
        newitem = array[i]
        childpos = 2 * i + 1

        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not array[childpos][0] < array[rightpos][0]:
                childpos = rightpos

            array[i] = array[childpos]
            i = childpos
            childpos = 2 * i + 1

        array[i] = newitem
        self.shift_down(array, startpos, i)

    def shift_down(self, array, startpos, i):
        newitem = array[i]

        while i > startpos:
            parentpos = (i - 1) >> 1
            parent = array[parentpos]
            if newitem[0] < parent[0]:
                array[i] = parent
                i = parentpos
                continue
            break
        array[i] = newitem

    def heap_pop(self, heap):
        lastelt = heap.pop()
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            self.sift_up(heap, 0)
            return returnitem
        return lastelt
