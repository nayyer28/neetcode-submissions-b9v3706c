class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        for string in strs:
            arr = [0] * 26
            
            for s in string:
                arr[ord(s) - 97] += 1
            
            arr = tuple(arr)

            if arr in hmap:
                hmap[arr].append(string)
            else:
                hmap[arr] = [string]
            
        out = []
        for v in hmap.values():
            if v:
                out.append(v)
        return out






        