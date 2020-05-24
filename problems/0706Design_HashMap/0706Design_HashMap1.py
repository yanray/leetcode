"""

Version: 1.1 
Author:  Yanrui 
date:    5/24/2020
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        if key in self.dict:
            self.dict[key] = value
        else:
            self.dict[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        if key in self.dict:
            return self.dict[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        if key in self.dict:
            del self.dict[key]
        

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

