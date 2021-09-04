class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left = [0]*len(arr) #left[i]表示以i为山顶，往左走到最远山脚的长度
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 0
        right = [0]*len(arr) #right[i]表示以i为山顶，往右到达最远山脚的长度
        for j in reversed(range(1,len(arr))):
            if arr[j-1]>arr[j]:
                right[j-1] = right[j]+1
            else:
                right[j-1] = 0

        max_l = 0
        for i in range(len(arr)):
            if left[i]>0 and right[i]>0:
                max_l = max(max_l,left[i]+right[i]+1)
        return max_l
