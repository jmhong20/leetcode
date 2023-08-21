class Solution:
  def findNextGreater(nums: list[int]) -> list[int]:
      index = [-1] * len(nums)
      nextGreater = list( [x, -1] for x in nums )
  
      prev = -1
      for i in range(len(nums)):
          if i == len(nums) - 1:
              nextGreater[i][1] = -1
          else:
              if nums[i + 1] > nums[i]:
                  nextGreater[i][1] = nums[i + 1]
                  while prev != -1:
                      if nums[i + 1] > nums[prev]:
                          nextGreater[prev][1] = nums[i + 1]
                          prev = index[prev]
                      else: break
              else:
                  index[i] = prev
                  prev = i
      return nextGreater
  
  def nextGreaterElement(nums1, nums2) -> list[int]:
      nums1 = list( [nums1[x], x] for x in range(len(nums1)) )
      nums1 = sorted(nums1, key = lambda x: x[0])
  
      nextGreater = findNextGreater(nums2)
      nextGreater = sorted(nextGreater, key = lambda x: x[0])
      answer = [-1] * len(nums1)
  
      i = j = 0
      while i < len(nums1) and j < len(nums2):
          if nums1[i][0] == nextGreater[j][0]:
              answer[nums1[i][1]] = nextGreater[j][1]
              i += 1
              j += 1
          else:
              if nums1[i][0] > nextGreater[j][0]:
                  j += 1
              elif nums1[i][0] < nextGreater[j][0]:
                  i += 1
  
      return answer
