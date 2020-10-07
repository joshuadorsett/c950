class HashTable:
    def __init__(self, startingCapacity=40):
        self._table = []
        for i in range(startingCapacity):
            self._table.append([None])
        self._size = 0

    def insert(self, key, value):
        hashedKey = hash(key) % len(self._table)
        # if index is found in table
        if self._table[hashedKey] is not None:
            self._table[hashedKey] = [key, value]
        # if index is not found in table
        else:
            self._table[hashedKey].append([key, value])
            self._size += 1

    def getValue(self, key):
        hashedKey = hash(key) % len(self._table)
        if self._table[hashedKey] is not None:
            return self._table[hashedKey][1]
        else:
            print("key not found")

    def getSize(self):
        return self._size

    def delete(self, key):
        hashedKey = hash(key) % len(self._table)
        self._table[hashedKey] = [None]
        self._size -= 1