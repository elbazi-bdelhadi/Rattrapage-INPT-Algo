class Solution(object):  
    def minimumSum(self,num):
        SortedNum = sorted([int(i) for i in list(str(num))])
        #The sorted() function returns a sorted list of the specified iterable object
        new1 = str(SortedNum[0]) + str(SortedNum[2])
        new2 = str(SortedNum[1]) + str(SortedNum[3])
        return int(new1) + int(new2)