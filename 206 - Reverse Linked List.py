class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
#Solution on Leetcode starts here -
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Your code goes here
        
    def printList(self, head: ListNode) -> ListNode:
        
        print(head.val)
        
        if head.next:
            newHead = self.printList(head.next)
        
def main():    
    ln3 = ListNode(3, None)
    ln2 = ListNode(2,ln3)
    ln = ListNode(1,ln2)
    
    soln = Solution()
    ans = soln.reverseList(ln)
    
    soln.printList(ans)
    
if __name__ == "__main__":
    main()
        