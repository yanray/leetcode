"""

Version: 1.1 
Author:  Yanrui 
date:    06/17/2020
"""

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def helper(image, i, j, original_color, new_color):
            
            nr = len(image)
            nc = len(image[0])
            
            if i < 0 or i >= nr or j < 0 or j >= nc or image[i][j] != original_color:
                return 
            
            image[i][j] = new_color
            helper(image, i - 1, j, original_color, new_color)
            helper(image, i + 1, j, original_color, new_color)
            helper(image, i, j - 1, original_color, new_color)
            helper(image, i, j + 1, original_color, new_color)

        if image[sr][sc] == newColor:
            return image
    
        new_image = image.copy()
        # new_image = image
        helper(new_image, sr, sc, image[sr][sc], newColor)
        
        return new_image


if __name__ == '__main__':

    a = Solution()

    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1 
    sc = 1
    newColor = 2
    print("Input: ", image)
    print("Output: ", a.floodFill(image, sr, sc, newColor))


