class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        print(m)
        print(n)
        for i in range(0,m):
            for j in range(0,n):
                if target==matrix[i][j]:
                    return True
                
        return False
#https://leetcode.com/problems/search-a-2d-matrix/
