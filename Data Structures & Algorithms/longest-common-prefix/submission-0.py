class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_wrd_sz=len(strs[0])
        ans=""
        for wrd in strs:
            min_wrd_sz=min(min_wrd_sz, len(wrd))
        
        for i in range(min_wrd_sz):
            letter=strs[0][i]
            for wrd in strs:
                if wrd[i]!=letter:
                    return ans
            
            ans+=letter
        
        return ans
        