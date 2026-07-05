class Solution:
    def checkAnagram(self, str1, str2) -> bool:
        # if sorted(str1) == sorted(str2):
        #     return True
        # else:
        #     return False
        alph_dict={}
        if len(str1) != len(str2):
            return False

        for i in str1:
            if i not in alph_dict:
                alph_dict[i]=0
            alph_dict[i]+=1
        
        for i in str2:
            if i not in alph_dict:
                return False
            alph_dict[i]-=1

            if alph_dict[i] < 0:
                return False
        
        return True
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[strs[0]]]
        n = len(strs)
        for i in range(1,n):
            flag=0
            for lis in ans:
                if self.checkAnagram(lis[0], strs[i]):
                    lis+=[strs[i]]
                    flag=1
                
                if flag == 1:
                    break
            if flag == 0:
                ans+=[[strs[i]]]

        return ans