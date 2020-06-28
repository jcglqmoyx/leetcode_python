from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        d = {}
        for domain in cpdomains:
            index = domain.index(' ')
            number = int(domain[:index])
            for i in range(len(domain) - 1, index - 1, -1):
                if domain[i] == ' ' or domain[i] == '.':
                    sub_domain = domain[i + 1:]
                    if sub_domain in d:
                        d[sub_domain] += number
                    else:
                        d[sub_domain] = number
        for key in d.keys():
            result.append(str(d[key]) + ' ' + key)
        return result
