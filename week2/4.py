class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=gain[0]
        s=0
        for i in range(len(gain)):
            s=s+gain[i]
            if maxi<s:
                maxi=s
                
        return maxi
