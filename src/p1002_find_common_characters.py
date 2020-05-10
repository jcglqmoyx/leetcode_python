# from typing import List, Dict


# class Solution:
#     def commonChars(self, A: List[str]) -> List[str]:
#         result = []
#         freq1 = self.freq(A[0])
#         for key, value in freq1.items():
#             min_freq = freq1[key]
#             for i in range(1, len(A)):
#                 if key in self.freq(A[i]):
#                     min_freq = min(self.freq(A[i])[key], min_freq)
#                 else:
#                     min_freq = 0
#             if min_freq:
#                 for i in range(0, min_freq):
#                     result.append(key)
#         return result

#     def freq(self, string: str) -> Dict[str, int]:
#         freq = {}
#         for c in string:
#             freq[c] = string.count(c)
#         return freq

#     def compare(self: Dict[str, int], freq2: Dict[str, int]) -> Dict[str, int]:
#         for key, value in self.items():
#             self[key] = min(self[key], freq2[key])
#         return self


import collections
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 1:
            return list(A[0])
        dic = collections.Counter(A[0])
        res = []
        for key, value in dic.items():
            for word in A[1:]:
                count = word.count(key)
                if not count:
                    value = 0
                if count <= value:
                    value = count
            if value:
                for i in range(value):
                    res.append(key)
        return res
