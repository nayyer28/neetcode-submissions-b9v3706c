class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        left, right = 0, len(A) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True: # left and right will cross over into outside the array ranges
            midA = (left + right) // 2
            midB = half - (midA + 1) - 1
            
            Aleft = A[midA] if midA >=0 else float("-inf")
            Aright = A[midA + 1] if midA + 1 < len(A) else float("inf")
            Bleft = B[midB] if midB >=0 else float("-inf")
            Bright = B[midB + 1] if midB + 1 < len(B) else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft <= Bright and Bleft > Aright:
                # 1 3 5 6 8 9 12 => B
                # 1 2 3 4 11 => A
                left = midA + 1
            else: # B[midB] <= A[midA+1] and A[midA] > B[midB+1]
                # 1 2 2 2 8 9 12 => B
                # 1 2 3 4 11 => A
                right = midA - 1
        

