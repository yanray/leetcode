"""

Version: 1.1 
Author:  Yanrui 
date:    5/24/2020
"""


class Bucket: 
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        found = False
        for i, key_value in enumerate(self.bucket):
            if key_value[0] == key:
                self.bucket[i] = (key, value)
                found = True
                # print('i', i)
                # print('key_value', key_value)

        if not found: 
            self.bucket.append((key, value))

        # print(self.bucket)

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v

        return -1

    def remove(self, key):
        for i, key_value in enumerate(self.bucket):
            if key_value[0] == key:
                del self.bucket[i]


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space_num = 2069
        self.hashtable = [Bucket() for i in range(self.key_space_num)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        hash_key = key % self.key_space_num
        self.hashtable[hash_key].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space_num
        return self.hashtable[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space_num
        self.hashtable[hash_key].remove(key)
        

if __name__ == '__main__':
    bb = MyHashMap()

    bb.put(1, 1)
    print('put (1, 1)')
    print('get: ', bb.get(1))

    bb.put(1, 10)
    print('put (1, 10)')
    print('get: ', bb.get(1))

    bb.put(12345, 111)
    print('put (12345, 111)')
    print('get: ', bb.get(12345))

