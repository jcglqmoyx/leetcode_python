from typing import List


# class Solution:
#     def shortestToChar(self, S: str, C: str) -> List[int]:
#         result = []
#         for i in range(len(S)):
#             if S[i] == C:
#                 result.append(0)
#                 continue
#             left = right = 0
#             j, k = i - 1, i + 1
#             l = r = False
#             while j >= 0:
#                 left += 1
#                 if S[j] == C:
#                     l = True
#                     break
#                 j -= 1
#             while k < len(S):
#                 right += 1
#                 if S[k] == C:
#                     r = True
#                     break
#                 k += 1
#             if left == 0:
#                 result.append(right)
#             elif right == 0:
#                 result.append(left)
#             else:
#                 if l and r:
#                     result.append(min(left, right))
#                 elif l:
#                     result.append(left)
#                 else:
#                     result.append(right)
#         return result

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        result = [0] * len(S)
        prev = -20000
        for i in range(len(S)):
            if S[i] == C:
                prev = i
            result[i] = i - prev
        prev = 20000
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            result[i] = min(result[i], prev - i)
        return result
