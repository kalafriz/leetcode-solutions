class Solution:
    def kthLargestLevelSum(self, root, k):
        # min heap of size k
        # at the end, top element is kth largest
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)

        while bfs_queue:
            # level order traversal
            size = len(bfs_queue)
            sum_val = 0
            for _ in range(size):
                popped_node = bfs_queue.popleft()
                sum_val += popped_node.val
                if popped_node.left is not None:
                    # add left child
                    bfs_queue.append(popped_node.left)
                if popped_node.right is not None:
                    # add right child
                    bfs_queue.append(popped_node.right)

            heapq.heappush(pq, sum_val)
            if len(pq) > k:
                # evict top element
                heapq.heappop(pq)
        if len(pq) < k:
            return -1
        return pq[0]