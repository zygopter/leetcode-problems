class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = ''
        for left in range(len(s)):
            currentLongestSubstring = ''
            for rigth in (range(left,len(s))):
                if s[rigth] in currentLongestSubstring:
                    if len(currentLongestSubstring) > len(longestSubstring):
                        longestSubstring = currentLongestSubstring
                    break
                currentLongestSubstring += s[rigth]
            if len(currentLongestSubstring) > len(longestSubstring):
                longestSubstring = currentLongestSubstring

        return len(longestSubstring)