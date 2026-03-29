class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                node = Node()
                curr.children[c] = node
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for w in words:
            trie.insert(w)

        ROWS = len(board)
        COLS = len(board[0])
        res = []
        def dfs(r:int, c:int, curr: Node, path: str):
            # bounds / visited / no trie path
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            ch = board[r][c]
            if ch == "." or ch not in curr.children:
                return
            

            curr = curr.children[ch]

            # found a word
            if curr.end:
                res.append(path+ch)
                curr.end = False

            # mark visited
            board[r][c] = "."

            dfs(r + 1, c, curr,path+ch)
            dfs(r - 1, c, curr,path+ch)
            dfs(r, c + 1, curr,path+ch)
            dfs(r, c - 1, curr,path+ch)

            # restore
            board[r][c] = ch
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,trie.root, "")
        return res
