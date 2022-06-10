# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# The key note is that since the interface is given above, we shall not use isinstance() 
# to check if the object is a NestedInteger or a list. We shall use the functions shown above.

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(nestedList):
            result = []
            for i in nestedList:
                if i.isInteger():
                    result.append(i.getInteger())
                else:
                    result += flatten(i.getList())
            return result
        
        self.lst = flatten(nestedList)
        

    def next(self):
        """
        :rtype: int
        """
        return self.lst.pop(0)
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.lst) > 0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())