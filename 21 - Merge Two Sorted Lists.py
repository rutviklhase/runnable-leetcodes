class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#-----------------------------------------------------------------------------------------------
#Solution on Leetcode starts here -    
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        #YOUR CODE GOES HERE
        
        
        
#-----------------------------------------------------------------------------------------------
    def printResultList(self, resList: ListNode):
        print(resList.val)
        if resList.next:
            self.printResultList(resList.next)
            

def main():
    #Creating two Lists - [5,6,7] and [1,2,3,4]
    ln7 = ListNode(7, None)
    ln6 = ListNode(6, ln7)
    ln5 = ListNode(5, ln6)
    ln4 = ListNode(4, None)
    ln3 = ListNode(3, ln4)
    ln2 = ListNode(2, ln3)
    ln1 = ListNode(1, ln2)
    
    soln = Solution()
    ans = soln.mergeTwoLists(ln1, ln5)
    soln.printResultList(ans) #Expected Output - [1,2,3,4,5,6,7]

if __name__ == "__main__":
    main()