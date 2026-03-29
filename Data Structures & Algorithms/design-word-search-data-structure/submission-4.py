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
        
        def dfs(j:int, r: Node) -> bool:
            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    for node in r.children.values():
                        if dfs(i+1,node):
                            return True
                    return False
                else:
                    if c not in r.children:
                        return False
                    r = r.children[c]
            return r.end
        return dfs(0,self.root)


