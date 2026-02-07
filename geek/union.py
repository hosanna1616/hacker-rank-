class Solution:
    def findUnion(self, a, b):
        return sorted(list(set(a) | set(b)))