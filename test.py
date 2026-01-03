def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        m = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            r = s[right]
            while (r in m):
                m.remove(s[left])
                left += 1
            m.add(r)
            max_len = max(max_len, right - left + 1)

        return max_len

            

print(lengthOfLongestSubstring("pwwkew"))