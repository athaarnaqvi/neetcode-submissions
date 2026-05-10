class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Count characters in t
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}
        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Check if character count matches
            if c in countT and window[c] == countT[c]:
                have += 1

            # Valid window
            while have == need:

                # Update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Remove left character
                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        left, right = res

        return s[left:right + 1] if resLen != float("inf") else ""