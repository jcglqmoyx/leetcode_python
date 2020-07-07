from typing import List


# class Solution:
#     def uncommonFromSentences(self, A: str, B: str) -> List[str]:
#         words1, words2 = A.split(' '), B.split(' ')
#         d1, d2 = {}, {}
#         for word in words1:
#             if word in d1:
#                 d1[word] += 1
#             else:
#                 d1[word] = 1
#         for word in words2:
#             if word in d2:
#                 d2[word] += 1
#             else:
#                 d2[word] = 1
#         result = []
#         for word in d1:
#             if d1[word] == 1 and word not in d2:
#                 result.append(word)
#         for word in d2:
#             if d2[word] == 1 and word not in d1:
#                 result.append(word)
#         return result

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words1, words2 = A.split(' '), B.split(' ')
        result = []
        for word in words1:
            if words1.count(word) == 1 and word not in words2:
                result.append(word)
        for word in words2:
            if words2.count(word) == 1 and word not in words1:
                result.append(word)
        return result
