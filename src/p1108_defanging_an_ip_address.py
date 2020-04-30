# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         ret = ''
#         for ch in address:
#             if ch == '.':
#                 ret += '[.]'
#             else:
#                 ret += ch
#         return ret

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.split(".")
        s = "[.]".join(address)
        return s