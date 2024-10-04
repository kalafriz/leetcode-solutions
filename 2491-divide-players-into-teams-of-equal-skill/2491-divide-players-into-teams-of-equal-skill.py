class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n = len(skill)
        
        if sum(skill)%(n/2) != 0: # Check if we can divide them into teams of equal skill
            return -1
        
        target = int(sum(skill)/(n/2))
        
        skillDict = defaultdict(list)
        for i,s in enumerate(skill): # Build skill:index hash for faster matching
            skillDict[s].append(i)
            
        chemistrySum = 0
        
        for player in skill:
            if player == -1: # player marked as already used
                pass
            else:
                skillDict[player] = skillDict[player][1:] # prevent further matches to this player

                matchVal = target - player
                if skillDict[matchVal]: # get matching player, add to result, and prevent being used again
                    match = skillDict[matchVal][0]
                    skillDict[matchVal] = skillDict[matchVal][1:]
                    print(player, match, matchVal)
                    chemistrySum += player*matchVal
                    skill[match] = -1
                else: # no matching player
                    return -1
            
        return chemistrySum