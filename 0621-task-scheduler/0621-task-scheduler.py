class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # INTUITION: We want to greedily select the tasks with the
        # max frequency, and then will be able to fit all other lower freq
        # tasks in those gaps
        
        # 1. Designate (n+1) space, (max freq-1) times
        # 2. Add an extra space at the end for each distinct max freq task.
        #    This accounts for the -1 in (max freq-1), since we don't need
        #    to wait (n+1) time for the final execution
        # 3. Any tasks with less than max freq will fit in the remaining space
        
        # EXCEPTION: There are more cycles needed for non-maxfreq tasks than
        #            max freq taks. In this case, the logic is flipped, where
        #            the max freq tasks can fit in the gaps of the non-max ones
        
        taskfreq = Counter(tasks)
        maxfreq = max(taskfreq.values())
        num_maxfreq = sum(1 for f in taskfreq.values() if f == maxfreq)
        
        cycles = (maxfreq-1) *(n+1) + num_maxfreq
        
        return max(cycles, len(tasks))