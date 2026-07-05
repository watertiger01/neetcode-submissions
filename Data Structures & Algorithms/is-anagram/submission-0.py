class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph_dict={}
        for i in range(len(s)):
            if s[i] not in alph_dict:
                alph_dict[s[i]]=0

            alph_dict[s[i]]+=1
        
        for i in range(len(t)):
            if t[i] in alph_dict:
                alph_dict[t[i]]-=1
                if alph_dict[t[i]]<0:
                    return False
            else:
                return False
        return True

