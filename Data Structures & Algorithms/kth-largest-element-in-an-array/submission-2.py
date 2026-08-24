class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-i for i in nums]


        heapq.heapify(nums)

        # print(nums)


        for i in range(k):
            x = heapq.heappop(nums)

        return -x