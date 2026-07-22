# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minheap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minheap,NodeWrapper(lst))
        
        res = ListNode(0)
        cur = res

        while minheap:
            min_ele = heapq.heappop(minheap)
            cur.next = min_ele.node
            cur = cur.next

            if cur.next:
                heapq.heappush(minheap,NodeWrapper(cur.next))
        
        return res.next
        