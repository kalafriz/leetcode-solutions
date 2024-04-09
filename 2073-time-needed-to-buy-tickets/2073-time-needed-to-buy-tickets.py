import numpy as np
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        # METHOD: Add number of non-zero people in line while k needs more than 1 to time.
        #         Subtract 1 from all people who need more than 0.
        #         Once k needs only 1, add sum of non-zero people in front of k to time.
        
        tickets = np.array(tickets)
        time = 0
        current = 0
        
        while tickets[k] > 1:
            
            time += np.count_nonzero(tickets)
            tickets = np.where(tickets > 0, tickets-1, tickets)
            #print(tickets)
        
        if tickets[k] == 1:
            
            time += np.count_nonzero(tickets[:k+1])
            
        return time