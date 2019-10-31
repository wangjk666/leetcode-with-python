 # 搜索二维矩阵，矩阵的特点是每一行从左往右递增，每一列从上到下递增
 # 分治法将矩阵四分
 def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_num=len(matrix)
        
        if row_num ==0:
            return False
        
        col_num=len(matrix[0])
        if col_num ==0:
            return False
        
        if matrix[0][0] == target:
            return True
        if matrix[-1][-1] == target:
            return True
        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False
        
        mid_row=int(row_num/2+0.51)
        mid_col=int(col_num/2+0.51)
        
        firstMatrix=[]
        
        for r_ind in range(mid_row):
            firstMatrix.append(matrix[r_ind][0:mid_col])
        
        if self.searchMatrix(firstMatrix,target) == True:
            return True
        
        secondMatrix=[]
        
        for r_ind in range(mid_row):
            secondMatrix.append(matrix[r_ind][mid_col:])
        
        if self.searchMatrix(secondMatrix,target) == True:
            return True
        
        thirdMatrix=[]
        
        for r_ind in range(mid_row,row_num):
            thirdMatrix.append(matrix[r_ind][0:mid_col])
        
        if self.searchMatrix(thirdMatrix,target) == True:
            return True

        fourthMatrix=[]
        
        for r_ind in range(mid_row,row_num):
            fourthMatrix.append(matrix[r_ind][mid_col:])
        
        if self.searchMatrix(fourthMatrix,target) == True:
            return True
                
        return False
        