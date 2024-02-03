# defining the Node class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# defining the function to swap pairs
def swapPairs(head):
    # creating a dummy node for convenience
    dummy = ListNode(0)
    # let the dummy node point to head
    dummy.next = head

    # creating a variable to keep track of the previous node
    prev_Node = dummy
    while head and head.next:
        # nodes to be swapped
        first_Node = head
        second_Node = head.next

        # swapping nodes
        prev_Node.next = second_Node
        first_Node.next = second_Node.next
        second_Node.next = first_Node

        # reinitialize the head and prev_Node for next swap
        prev_Node = first_Node
        head = first_Node.next

    # return the new head
    return dummy.next