"""
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

 

Example 1:


Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
Example 2:


Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.
 

Constraints:

The tree consists only of the root, its left child, and its right child.
-100 <= Node.val <= 100
"""
class Solution(object):  
    def minimumSum(self,num):
        SortedNum = sorted([int(i) for i in list(str(num))])
        #The sorted() function returns a sorted list of the specified iterable object
        new1 = str(SortedNum[0]) + str(SortedNum[2])
        new2 = str(SortedNum[1]) + str(SortedNum[3])
        return int(new1) + int(new2)
