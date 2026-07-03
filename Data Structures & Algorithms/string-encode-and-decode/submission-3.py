class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return '\t'
        return '\n'.join(strs)
    
    def decode(self, s: str) -> List[str]:
        if s == '\t':
            return []
        return s.split('\n')

