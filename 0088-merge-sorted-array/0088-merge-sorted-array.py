class Solution:

  def merge(
      self, nums1: list[int], m: int, nums2: list[int], n: int
  ) -> None:
    """Do not return anything, modify nums1 in-place instead."""
    # Pointers for nums1, nums2, and the placement index from the end
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    # Compare elements from the back and place the larger one at index p
    while p1 >= 0 and p2 >= 0:
      if nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
      else:
        nums1[p] = nums2[p2]
        p2 -= 1
      p -= 1

    # If any elements remain in nums2, copy them over
    # (Remaining elements in nums1 are already in their correct places)
    while p2 >= 0:
      nums1[p] = nums2[p2]
      p2 -= 1
      p -= 1