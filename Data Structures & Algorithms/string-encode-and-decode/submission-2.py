class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return '\t'
        print('\n'.join(strs))
        return '\n'.join(strs)
    
    def decode(self, s: str) -> List[str]:
        if s == '\t':
            return []
        print(s)
        print(s.split('\n'))
        return s.split('\n')

