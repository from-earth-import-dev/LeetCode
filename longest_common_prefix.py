'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

class Solution:    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        j = 0

        def strComparison(str1, str2, j, n):
            str1_len = len(str1)
            str2_len = len(str2)
            
            if j+1 == n: # last comparision, base case
                if str1 == '':
                    return '' # Empty str means no common prefix, return
                else:
                    if str1_len >= str2_len:
                        for i in range(str1_len):
                            if i == str2_len:
                                return str1[:i]
                            else:
                                if str1[i] != str2[i]:
                                    return str1[:i]
                        return str1
                    else:
                        for i in range(str2_len):
                            if i == str1_len:
                                return str2[:i]
                            else:
                                if str1[i] != str2[i]:
                                    return str2[:i]

            else:
                if str1_len == 0:
                    return '' # Empty str means no common prefix, return
                else:
                    if str1_len >= str2_len:
                        for i in range(str1_len):
                            if i == str2_len:
                                return strComparison(str1[:i], strs[j+1], j+1, n)
                            else:
                                if str1[i] != str2[i]:
                                    return strComparison(str1[:i], strs[j+1], j+1, n)
                        return strComparison(str1, strs[j+1], j+1, n)
                    else:
                        for i in range(str2_len):
                            if i == str1_len:
                                return strComparison(str1[:i], strs[j+1], j+1, n)
                            else:
                                if str1[i] != str2[i]:
                                    return strComparison(str1[:i], strs[j+1], j+1, n)

        if n == 1:
            return strs[0]
        else:
            for j in range(n):
                return strComparison(strs[j], strs[j+1], j+1, n)
