## Flood Fill

### Problem Link

https://leetcode.com/problems/flood-fill/

### Problem Description 

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

```
Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

```

**Note:**

* The length of image and image[0] will be in the range [1, 50].
* The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
* The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

### How to solve 

**Approach 1:**

判断长度, 解决长度不等的问题, 判断node是否相等

**Approach 2:**

Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.

* Complexity Analysis

    - Time complexity : O(m+n)O(m+n).

    - Space complexity : O(m)O(m) or O(n)O(n).

**Approach 3:**

**Approach 4:**

* Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.

* When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pBpB reaches the end of a list, redirect it the head of A.
*  If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.

*  To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), pBpB would reach the end of the merged list first, because pBpB traverses exactly 2 nodes less than pApA does. By redirecting pBpB to head A, and pApA to head B, we now ask pBpB to travel exactly 2 more nodes than pApA would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.

* If two lists have intersection, then their last nodes must be the same one. So when pApA/pBpB reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.

**Approach 5:**

A trick to this problem

**Approach 6:**

Use set()



### Code (python)

[Approach 1]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        len_A = 0
        node_A = headA
        while node_A.next:
            node_A = node_A.next
            len_A += 1
            
        len_B = 0
        node_B = headB
        while node_B.next:
            node_B = node_B.next
            len_B += 1
            
        if node_A.val != node_B.val:
            return None
        
        node_A = headA
        node_B = headB
        if len_A > len_B:
            for _ in range(len_A - len_B):
                node_A = node_A.next
        elif len_A < len_B:
            for _ in range(len_B - len_A):
                node_B = node_B.next
                
        while node_A != node_B:
            node_A = node_A.next
            node_B = node_B.next
        
        return node_A
```

[Approach 2]

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dictA={}
        # step 1: travel headA, and storaged each node in a dict
        while headA:
            dictA[headA] = 0
            headA = headA.next
        # step 2: travel headB, check each node if in dict 
        while headB:
            # if checked, return the headB node = intersctionNode
            if headB in dictA:
                return headB
            headB = headB.next
        #No checked, no found intersctionNode
        return None
```


[Approach 3]

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        arr_1, arr_2 = [], []
        while headA:
            arr_1.append(headA)
            headA = headA.next
        while headB:
            arr_2.append(headB)
            headB = headB.next
        b = len(arr_2) - 1 
        if arr_1[len(arr_1)-1] != arr_2[b]:
            return None
        for i in range(len(arr_1)-1,-1,-1):
            if arr_1[i] != arr_2[b]:
                return(arr_1[i + 1])
            b -= 1
        return arr_1[0]
```

[Approach 4]

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        cycle_counter = 0
        while pa is not None and pb is not None:
            if pa == pb:
                return pa
            if pa.next is None:
                cycle_counter += 1
                if cycle_counter == 2:
                    return None
            pa = (pa.next if pa.next is not None else headB)
            pb = (pb.next if pb.next is not None else headA)
        
        return None
```

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #a+c+b=b+c+a
        l1,l2=headA,headB
        while l1!=l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
```

[Approach 5]

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #Negate all vals of listA and stop at first -ve val encountered in listB
        if not headA or not headB:
            return None
        key=headA
        while headA:
            headA.val= -1*headA.val
            headA=headA.next
        while headB and headB.val>=0:
            headB=headB.next
        #Again original vals are restored as the testbench checks for
        #any modification in the list
        while key:
            key.val=-1*key.val
            key=key.next
        return headB
```

[Approach 6]

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        temp1 = headA
        temp2 = headB
        
        A_set = set()
        B_set = set()
        
        while temp1 and temp2:
            A_set.add(temp1)
            B_set.add(temp2)
            
            if temp1 in B_set:

                return temp1
            elif temp2 in A_set:

                return temp2
            
            temp1 = temp1.next
            temp2 = temp2.next  
        
        if temp1:
            while temp1:
                if temp1 in B_set:
                    return temp1
            
                temp1 = temp1.next  
        
        if temp2:
            while temp2:
                if temp2 in A_set:
                    return temp2

                temp2 = temp2.next
        
        return None 
```

```python
class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> ListNode:
        S = set()
        while A != None: A, _ = A.next, S.add(A) 
        while B != None:
            if B in S: return B
            B = B.next
```