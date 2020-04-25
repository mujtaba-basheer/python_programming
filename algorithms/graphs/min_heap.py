class MinHeap(object):

    def __init__(self, arr = list()):
        self.array = [x[1] for x in arr]
        self.elems = [x[0] for x in arr]
        self.length = len(self.array)
        self.pos = { self.elems[i]: i for i in range(self.length) }
        if self.length > 0:
            self.build_min_heap()

    def build_min_heap(self):
        for i in range(int(self.length / 2) - 1, -1, -1):
            self.min_heapify(i)

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

        self.pos[self.elems[i]] = j
        self.pos[self.elems[j]] = i

        temp = self.elems[i]
        self.elems[i] = self.elems[j]
        self.elems[j] = temp

    def check_up(self, i):
        if i == 0:
            return True
        p_ind = int((i - 1) / 2)
        return (p_ind >= 0 and self.array[i] >= self.array[p_ind])

    def check_down(self, i):
        child1, child2 = i * 2 + 1, i * 2 + 2
        n = self.length
        if child1 > n - 1:
            return True
        return (child1 < n and self.array[i] < self.array[child1] or child2 < n and self.array[i] < self.array[child2])

    def min_heapify(self, i = 0):
        ind = i * 2 + 1
        n = self.length
        while self.check_down(i) == False:
            min_ind = ind + 1 if ind + 1 < n and self.array[ind + 1] < self.array[ind] else ind
            self.swap(i, min_ind)
            i = min_ind
            ind = i * 2 + 1

    # def insert(self, k):
    #     self.array.append(k[1])
    #     self.elems.append(k[0])
    #     self.length += 1
    #     self.bubble_up(self.length - 1)
    
    def bubble_up(self, i):
        while self.check_up(i) == False:
            p_ind = int((i - 1) / 2)
            self.swap(i, p_ind)
            i = p_ind

    def decrease_key(self, v, k):
        i = self.pos[v]
        self.array[i] = k
        self.bubble_up(i)

    def extract_min(self):
        n = self.length
        if n == 0:
            return None
        
        min_elem = self.elems[0]
        self.swap(0, n - 1)
        self.array.pop()
        self.elems.pop()
        del self.pos[min_elem]
        self.length -= 1
        self.min_heapify()
        return min_elem

    def get_length(self):
        return self.length

    def enumerate(self):
        for x in self.array:
            print(x, end = " ")
        print()