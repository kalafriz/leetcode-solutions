class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        result = []
        
        # METHOD: Build the deck as it would be revealed.
        if len(deck) <=1:
            return deck
        
        for i in range(len(deck)-1, -1, -1):
            
            # Move bottom card to top
            if i != len(deck)-1:
                result = [result[-1]] + result[:-1]
            
            # Add next card from sorted deck to top
            result = [deck[i]]+result
            
            #print(result)
            
        return result