from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = []
        for email in emails:
            index_at = email.index('@')
            email = email[:index_at].replace('.', '') + email[index_at:]
            index_at = email.index('@')
            if email.__contains__('+'):
                email_set.append(email[:email.index('+')] + email[index_at:])
            else:
                email_set.append(email)
        return len(set(email_set))
