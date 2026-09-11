class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0
        best_len = float("inf")
        best_start = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            # Character has reached the required frequency
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Current window contains all required characters
            while formed == required:
                # Update answer
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                # Remove leftmost character
                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]