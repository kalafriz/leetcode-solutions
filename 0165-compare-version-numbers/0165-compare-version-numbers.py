class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        #print(v1, v2)
        
        for i in range(max(len(v1), len(v2))):
            
            n1 = int(v1[i]) if len(v1)>i else 0
            n2 = int(v2[i]) if len(v2)>i else 0
            
            #print(n1,n2)
            
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            # else n1==n2 continue
        
        return 0