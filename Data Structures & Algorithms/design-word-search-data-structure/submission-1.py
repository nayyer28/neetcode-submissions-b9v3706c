class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(w:str, r: Node) -> bool:
            p = 0
            while p < len(w):
                c = w[p]
                if c == '.':
                    res = False
                    for node in r.children.values():
                        res = res or dfs(w[p+1:],node)
                    return res
                elif c not in r.children:
                    return False
                r = r.children[c]
                p += 1
            return r.end
        return dfs(word,self.root)


