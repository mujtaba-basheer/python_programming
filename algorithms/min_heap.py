class MinHeap(object):

    def __init__(self, arr = list()):
        self.array = arr
        self.length = len(self.array)

    def build_min_heap(self):
        for i in range(int(self.length / 2) - 1, -1, -1):
            self.max_heapify(i)

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

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

    def insert(self, k):
        self.array.append(k)
        i = self.length
        self.length += 1
        while self.check_up(i) == False:
            p_ind = int((i - 1) / 2)
            self.swap(i, p_ind)
            i = p_ind

    def extract_min(self):
        n = self.length
        if n == 0:
            return None
        
        min_val = self.array[0]
        self.swap(0, n - 1)
        self.array.pop()
        self.length -= 1
        self.min_heapify()
        return min_val

    def enumerate(self):
        for x in self.array:
            print(x, end = " ")
        print()