class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for word in words for c in word}

        for i in range(len(words) -1 ):
            word1 = words[i]
            word2 = words[i+1]

            minword = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minword] == word2[:minword]:
                return ""

            for j in range(minword):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        res = []
        visited = {}
        
        def dfs(word):
            if word in visited:
                return visited[word]
                
            visited[word] = True

            for nei in adj[word]:
                if dfs(nei):
                    return True
                    
            visited[word] = False
            res.append(word)

        for char in adj:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)