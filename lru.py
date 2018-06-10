
class LRU(object):
    def __init__(self, size):
        self.size = size
        self.cache = {}
        self.recent = []

    def __repr__(self):
        return "LRU(%s)" % self.size

    def get(self, key):
        if key in self.cache:
            self.recent.remove(key)
            self.recent.append(key)
            return self.cache[key]
        else:
            return -1

    def print_lru(self):
        print(self.recent)

    def put(self, key, value=0):
        if len(self.recent) < self.size:
            self.recent.append(key)
            self.cache[key] = value
        else:
            if key in self.cache:
                self.get(key)
                return
            lru = self.recent[0]
            self.recent.remove(lru)
            self.recent.append(key)
            del self.cache[lru]
            self.cache[lru] = key


lru = LRU(4)
lru.put('a')
lru.put('b')
lru.put('c')
lru.put('d')
lru.put('e')
lru.put('d')
lru.put('f')
lru.print_lru()
