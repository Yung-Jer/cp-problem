# TLE
from collections import defaultdict
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList:
            return []
        graph = defaultdict(set)
        wordList.append(beginWord)
        n = len(wordList)
        
        for i in range(n):
            for j in range(i+1, n):
                a, b = wordList[i], wordList[j]
                if sum([char1 != char2 for char1, char2 in zip(a, b)]) == 1:
                    graph[a].add(b)
                    graph[b].add(a)
                    
        path = defaultdict(list) # each value is a list of the shortest path from beginWord to the key
        path[beginWord].append([beginWord])
        
        q = deque([(beginWord, [beginWord])]) # element: (node, path)
        visited = set()
        
        while q:
            word, cur_path = q.popleft()
            visited.add(word)
            for nxt in (w for w in graph[word] if (w not in path) or (len(path[w][-1]) == len(cur_path)+1)):
                if nxt not in visited:
                    nxt_path = cur_path + [nxt]
                    path[nxt].append(nxt_path)
                    if nxt != endWord:
                        q.append((nxt, nxt_path))
        return path[endWord]
