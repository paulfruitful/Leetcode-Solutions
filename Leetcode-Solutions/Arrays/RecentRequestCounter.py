class RecentCounter(object):

    def __init__(self):
        self.reqs=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.reqs and self.reqs[0]<t-3000:
            self.reqs.pop(0)
        self.reqs.append(t)
        return len(self.reqs)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
