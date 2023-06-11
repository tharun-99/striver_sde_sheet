def searchMatrix(mat: list(list(int)), target: int) -> bool:
    # Write your code here.
    m,n = len(mat), len(mat[0])
    top, bottom = 0, m-1
    left, right = 0, n-1
    while top <= bottom:
        mid_row = (top+bottom)//2
        if mat[mid_row][0] <= target and target <= mat[mid_row][n-1]:
            while left <= right:
                mid = (left+right)//2
                if mat[mid_row][mid] == target:
                    return True
                elif mat[mid_row][mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return False
        elif target > mat[mid_row][n-1]:
            top = mid_row+1
        else:
            bottom = mid_row-1
    return False