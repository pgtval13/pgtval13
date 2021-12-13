class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def deleteAtIndex(self, index):
    if index >= self.length or index < self.length:
        return

    cur_node = self.head
    if index == 0:
        self.head = self.head.next
    
    else:
        for _ in range(index-1):
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
    
    self.length -= 1

def hasCycle(self, head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

def removeNthFromEnd(self, head, n):
    dummy = ListNode(0,head) #initialize left pointer at zero
 #value doesnt matter
 #next pointer set to head of the list because its inserted at the beginning
    left = dummy #mover pointer
    right = head
    #we need head + n for right pointer, below is the implem
    while n > 0 and right: #know why, why not right.next
        right = right.next #keep shifting right
        n -= 1
    
    while right: #keep shifting until right reaches null
        left = left.next
        right = right.next
    
    #delete the node = update the pointer, skipping item to be deleted
    left.next = left.next.next
    #return next since we dont want to include the added dummy node
    return dummy.next

def mergeTwoLists(self, List1, List2):
    dummy = ListNode() #edge case of inserting into an empty list
    result = dummy

    while List1 and List2: #iterate while both list are not empty, so we can compare
        if List1.val > List2.val: #compare values
            result.next = List2 #add the node itself in the result
            List2 = List2.next #update List2 pointer
        else:
            result.next = List1
            List1 = List1.next
        result = result.next #update result pointer regardless of which node was inserted
    
    if List1: #if List1 is not yet empty, insert the remaining at the end of result
        result.next = List1
    elif List2:
        result.next = List2
    
    return dummy.next

def addTwoNumbers(self, l1, l2):
    dummy = ListNode() #for cases of inserting into a linked list
    curr = dummy #pointing to position of the new digit
    carry = 0
    while l1 or l2 or carry: #carry here is to continue the loop for cases like 7+8
        v1 = l1.val if l1 else 0 #value if not null, if null set to zero
        v2 = l2.val if l2 else 0 #value if not null, if null set to zero
       
        val = v1 + v2 + carry #compute the new digit
        
        carry = val // 10 #take the carry
        val = val % 10 #take the ones digit

        curr.next = ListNode(val) #insert result into the list

        #update the pointers
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

def removeElements(self, head, val):
    dummy = ListNode(next=head) #value does not matter 
    #next should be pointing to head(dummy node inserted right before head)
    prev, curr = dummy, head #prev is initally at left of curr
    
    while curr: #iterate through the list while curr is not None
        nxt = curr.next #store the next pointer in a variable
        if curr.val == val:
            prev.next = nxt #to delete the node, move the pointer from curr to curr.next 
        else:
            prev = curr #if not removing, move previous to the right
        curr = nxt #regardless if node is deleted or not, curr must be updated/shifted to next pointer
    return dummy.next #return new head
    #dummy is a node that will not be deleted, it always will point at the 1st node of the linked list

def reverseList(self, head):
    prev, cur = None, head
    #Using 2 Pointers
    #Store None to prev, store head node to cur
    while cur: #iterate to the Linked List
        nxt = cur.next
        cur.next = prev #point the next pointer of current node to prev
        prev = cur #move prev to curr node
        cur = nxt #move cur node to next node, saved in the nxt variable before movement of pointer
    return prev #new head node will be the last node on prev

def reverseList(self, head):
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead

def reorderList(self, head):
    #find the middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next #as fast reaches end of the list, slow will be at the middle
    
    #reverse the second half
    second = slow.next #beginning of the 2nd half
    slow.next = None #splitting into 2 different lists
    prev = None #temp for reversing the 2nd half
    while second:
        tmp = second.next #save pointer for updating later, as pointer will be reversed on next line
        second.next = prev #reverse the pointer
        prev = second #update 1st pointer
        second = tmp #update 2nd pointer
    
    #merge the two halves
    second = prev #beginning of 2nd list is last node of 2nd half, which is the head of prev
    first = head
    while second: #usually second is shorter
        tmp1, tmp2 = first.next, second.next #save pointer for updating later, pointer will be reassigned on next line
        first.next = second #inserting the second node in between first and first.next
        second.next = tmp1 # first > second > first.next
        first, second = tmp1, tmp2 #update the 2 pointers

class MyCircularQueue:
    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.head = None
        self.tail = None
    def enQueue(self, val: int) -> bool:
        if self.isFull(): return False
        newNode = ListNode(val)
        if self.isEmpty(): self.head = self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = self.head.next
        self.size -= 1
        return True
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val
    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size == self.maxSize