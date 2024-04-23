class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # METHOD:
        # Find all leaf nodes
        #   -> nodes with only 1 connection
        # "Prune" the leaf nodes each turn, and move onto the next set of nodes up the branch.
        # Keep pruning until we are left with the MHTs
        #   -> We can only have one or two MHTs. We know we're done when we only have one or two left.
        
        if not edges: # only 1 node
            return [0]
        
        edgeMap = defaultdict(set)
        mhtNodes = []
        
        # build map
        for u, v in edges:
            edgeMap[u].add(v)
            edgeMap[v].add(u)       
                
        # find leaf nodes
        for node, children in edgeMap.items():
            if len(children)==1:
                mhtNodes.append(node)
                
        while n > 2:
            n -= len(mhtNodes)
            
            childNodes = []
            
            for u in mhtNodes:
                v = next(iter(edgeMap[u]))
                edgeMap[v].remove(u)
                if len(edgeMap[v]) == 1: # leaf
                    childNodes.append(v)
                    
            mhtNodes = childNodes
            
            
            
        return mhtNodes