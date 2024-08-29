class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        cols = defaultdict(list)
        rows = defaultdict(list)
        
        #  BUILD GRAPH
        for r,c in stones:
            rows[r].append(c)
            cols[c].append(r)
            
        visited = set()
        count = 0 # count of connected node components
        
        # DFS
        for r,c in stones:
            if (r,c) not in visited:
                visited.add((r,c))
                queue = deque([(r,c)]) # nodes to visit
                
                while queue:
                    cr, cc = queue.popleft() # current node
                    # VISIT NEIGHBORS
                    for nc in rows[cr]: # for col of neighbors in current row
                        if (cr, nc) not in visited:
                            queue.append((cr, nc))
                            visited.add((cr, nc))
                            
                    for nr in cols[cc]: # for row of neighbors in current col
                        if (nr, cc) not in visited:
                            queue.append((nr, cc))
                            visited.add((nr, cc))
                
                # Queue has ended, we have hit all connected nodes in this component
                count +=1 
                
        return len(stones) - count