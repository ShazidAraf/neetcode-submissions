class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        if beginWord not in wordList:
            wordList.append(beginWord)


        def dist(w1,w2):
            count = 0
            for c1,c2 in zip(w1,w2):
                if c1!=c2:
                    count+=1
            return count

        graph = collections.defaultdict(list)

        for i in range(len(wordList)):
             for j in range(i+1,len(wordList)):

                d = dist(wordList[i],wordList[j])

                if d==1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        # print(graph)

        minheap = [(0,beginWord)]
        visit = set()
        res = []
        
        while minheap:

            cost, word = heapq.heappop(minheap)

            if word in visit:
                continue

            if dist(endWord,word)==0:
                return cost+1

            visit.add(word)
            res.append(word)

            for nei in graph[word]:
                if nei in visit:
                    continue
                heapq.heappush(minheap,(cost+1,nei))


        return 0
        