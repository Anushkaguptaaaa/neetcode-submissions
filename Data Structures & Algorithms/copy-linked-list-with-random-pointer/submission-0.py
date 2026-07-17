class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToCopy = {}

        
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

       
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy.get(curr.next)
            copy.random = oldToCopy.get(curr.random)
            curr = curr.next

        return oldToCopy[head]
        