class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # bin search is O(log N) --> keep N small
        if len(nums1) > len(nums2):
            A , B = nums2, nums1
        else:
            A, B = nums1, nums2
        
        total = (len(A) + len(B))
        half = total // 2
        
        lA, rA = 0, len(A) - 1

        while True:
            # partitions
            partA = (lA + rA) // 2
            partB = half - (partA + 1) - 1

            # handle boundary edge cases 
            Aleft = A[partA] if partA >= 0 else float("-inf")
            Aright = A[partA + 1] if partA + 1 < len(A) else float("inf")

            Bleft = B[partB] if partB >= 0 else float("-inf")
            Bright = B[partB + 1] if partB + 1 < len(B) else float("inf")

            # check partition validity

            if Aleft <= Bright and Bleft <= Aright:
                break # valid partition registered
            elif Aleft > Bright:
                rA = partA - 1
            else:
                lA = partA + 1
        
        # handle median return
        if total % 2 == 0: # even
            return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
        else:
            return (min(Aright, Bright))
        




            




