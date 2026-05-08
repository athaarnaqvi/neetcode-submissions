class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        right = 0
        left = 0
        maxfreq = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1

            maxfreq = max(maxfreq, count[s[right]])

            if (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            right += 1

        return right - left