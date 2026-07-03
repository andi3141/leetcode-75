class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        sorted_strs = [''.join(sorted(s)) for s in strs]
        print(sorted_strs)
        o = {}  # standardized string -> List[strings]
        for i in range(len(strs)):
            s = strs[i]
            ss = sorted_strs[i]
            print(s)
            print(ss)
            if ss in o:
                o[ss].append(s)
            else:
                o[ss] = [s]

        return list(o.values())

        
