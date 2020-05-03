# nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
#
#
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ransom_note_value, magazine_value = 1, 1
#         for ch in ransomNote:
#             index = ord(ch) - 97
#             ransom_note_value *= nums[index]
#         for ch in magazine:
#             index = ord(ch) - 97
#             magazine_value *= nums[index]
#         return magazine_value % ransom_note_value == 0


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for ch in ransomNote:
#             if magazine.count(ch) < ransomNote.count(ch):
#                 return False
#         return True


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote)
        for k, v in count.items():
            if magazine.count(k) < v:
                return False
        return True
