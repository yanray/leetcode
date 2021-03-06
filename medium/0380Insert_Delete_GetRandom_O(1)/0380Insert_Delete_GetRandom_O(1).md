## Insert Delete GetRandom O(1)

### Problem Link

https://leetcode.com/problems/insert-delete-getrandom-o1/

### Problem Description 

Design a data structure that supports all following operations in average O(1) time.


1. insert(val): Inserts an item val to the set if not already present.
2. remove(val): Removes an item val from the set if present.
3. getRandom: Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

```
Example 1:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

```

### Code (python)

[Approach 1] (%)

```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_dict = {}
        self.hash_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_dict:
            return False
        else:
            self.hash_dict[val] = len(self.hash_list)
            self.hash_list.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hash_dict:
            last_item = self.hash_list[-1]
            index = self.hash_dict[val]
            
            self.hash_list[index] = last_item
            self.hash_dict[last_item] = index
            
            self.hash_list.pop()
            del self.hash_dict[val]
            
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.hash_list)
```

```python

101leetcode's avatar
101leetcode
444
Last Edit: June 22, 2020 3:03 PM

106 VIEWS

class RandomizedSet:
    ## RC ##
    ## APPROACH : HASHMAP ##
    #   1. Insertion operation in list is O(1) but not deletion
    #   2. So we create one Hashmap with key,index and other list
    #   3. for deleting we go to hashmap, get index, go to that index in list, swap that element with last element.
    #   4. save the index to last element in hashmap and delete list last element

    def __init__(self):
        self.lists = []
        self.hmap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if(val in self.hmap):
            return False
        self.hmap[val] = self.length
        self.length += 1
        self.lists.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.hmap):
            return False
        index = self.hmap[val]
        self.hmap[self.lists[-1]] = index
        self.lists[index], self.lists[-1] = self.lists[-1], self.lists[index]
        self.lists.pop()
        self.hmap.pop(val)
        self.length -= 1
        return True

    def getRandom(self) -> int:
        ri = random.randint(0, self.length - 1)
        return self.lists[ri]
```


