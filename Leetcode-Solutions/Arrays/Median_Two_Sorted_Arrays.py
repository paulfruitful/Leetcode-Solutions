class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       #Merge the arrays
        array=nums1+nums2
       #Resort
        array=sorted(array)
       #Finding Median of Even lengths
        if(len(array)%2==0):
          m=len(array)/2
          sub=m-1
          sum=array[sub]+array[m]
          median=sum*0.5
          return median
        #Finding Median of Odd lengths
        elif(not len(array)%2==0):
          subMedian=len(array)/2
          median=array[subMedian]
          return median
