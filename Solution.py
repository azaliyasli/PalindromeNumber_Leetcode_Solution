class Solution(object):
    def isPalindrome(self, x):
        llist = []
        palindromeNum = 0

        if x >= 0:
            while x > 0:
                temp = x % 10
                llist.append(temp)
                x = x / 10

            originalList = llist[:]
            llist.reverse()

            if originalList == llist:
                return True
            else:
                return False
                
        else:
            return False
