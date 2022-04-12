class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a={}
        c=0
        for x in jewels:
            a[x]=1;
        for j in stones:
            if a.get(j):
                c+=1
        return c
#https://leetcode.com/problems/jewels-and-stones/
