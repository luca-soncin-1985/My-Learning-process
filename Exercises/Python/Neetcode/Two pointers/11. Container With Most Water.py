class Solution:
    def maxArea(self, h: List[int]) -> int:
        d = []
        for i in range(len(h)-1):
            l = []
            for j in range(i+1, len(h)):
                m = min(h[i], h[j])
                v = m * (j-i)
                l.append(v)
            d.append(max(l))
        return max(d)