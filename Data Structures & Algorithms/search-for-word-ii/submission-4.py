class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    
    def addword(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)
        
        rows, cols = len(board), len(board[0])
        res, seen = set(), set()

        def dfs(r, c, node, word):
            if r >= rows or c >= cols or min(r,c) < 0 or board[r][c] not in node.children or (r,c) in seen:
                return
            
            seen.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.isword:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            seen.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)