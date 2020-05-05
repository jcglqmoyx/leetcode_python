class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(A) > len(set(A)):
            return True
        count = 0
        indices = []
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                indices.append(i)
                if count > 2:
                    return False
        if len(indices) != 2:
            return False
        return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]
