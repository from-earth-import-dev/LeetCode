'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': # Empty string
            return 0
        if len(s) == 1: # Only one element
            return 1

        i = 0
        j = 1

        substr = s[i] # substring starts with first char in s
        max_substr_len = 1 # length of max substr
        temp_substr_len = 1 # length of sliding window substr

        while i + max_substr_len < len(s):
            while j <= len(s) - 1 and s[j] not in substr: # Slide window until char repeats or reach end of str
                substr += s[j]
                temp_substr_len += 1
                j += 1
            if temp_substr_len > max_substr_len: # If that's the new largest substr, store it as max
                max_substr_len = temp_substr_len 
                temp_substr_len = 1 # Reset temp_substr_len back to 1
            i += 1 # Move i over by 1
            j = i + 1 # Move j in front of i
            substr = s[i] # Reset substr
            temp_substr_len = 1 # Reset temp_substr_len back to 1

        return max_substr_len
