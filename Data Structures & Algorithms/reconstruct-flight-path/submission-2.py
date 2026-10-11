class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:


        graph = collections.defaultdict(list)

        for src,dst in sorted(tickets,reverse=True):
            graph[src].append(dst)

        # print(graph)

        res = []


        def dfs(a):


            

            while graph[a]:
                dfs(graph[a].pop())
            res.append(a)

        dfs("JFK")
        return res[::-1]



